import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle
import sys
from config import *
from utils import *

class DataAnalyzer:
    def __init__(self):
        self.df = None
        self.history = []
        self.current_fig = 0

    def load_csv(self, path):
        try:
            self.df = pd.read_csv(path)
            return True
        except Exception as e:
            return f"Error loading CSV: {str(e)}"

    def generate_code(self, query):
        query=generate_code_query.format(columns=list(self.df.columns), query=query)
        response,history = get_chat_completion(query, self.history)
        self.history = history
        code=self._extract_code(response)
        return code
    
    def debug_code(self,result,query,code):
        query=error_prompt.format(error=result['message'],query=query,code=code)
        response, history = get_chat_completion(query, self.history)
        self.history = history
        code=self._extract_code(response)
        return code

    def execute_code(self, code):
        if code is None:
            return {"status": "error", "message": "No code to execute.Please regenerate your code."}
        try:
            env = {'df': self.df,'plt':plt}
            exec(code, env)
            outcome={}
            for key,value in env.items():
                if key not in ['df','plt']:
                    try:
                        pickle.dumps(value)
                        outcome[key]=value
                    except (pickle.PicklingError, TypeError):
                        continue
            if plt.gcf().get_axes():
                img_path = f"outcome/plot_{self.current_fig}.png"
                plt.savefig(img_path)
                plt.close()
                self.current_fig += 1
                outcome['plot'] = img_path
            return {"status": "success",'outcome':outcome}
        except Exception as e:
            return {"status": "error", "message": str(e), "traceback": sys.exc_info()}

    def _extract_code(self, response):
        if '```python' in response:
            code = response.split('```python')[1].split('```')[0]
        else:
            code = "None"
        return code 
    
    def get_queries(self):
        queries=[]
        #return ["分析 Clothing 随时间变化的总销售额趋势.","对 bikes 进行同样的分析","哪些年份 components 比 accessories 的总销售额高?"]
        while True:
            query = input("请输入问题。如果没有问题，请输入exit：")
            if query == "exit":
                break
            queries.append(query)
        return queries
    
    def get_file(self):
        path=input('please enter the csv file path and "exit" to exit:')
        if path == "exit":
            exit()
        if not os.path.exists(path):
            print("文件不存在")
            return self.get_file()
        try:
            self.df = pd.read_csv(path)
        except Exception as e:
            print(f"文件读取失败:{e}")
            return self.get_file()
        return path
    
def main():
    analyzer = DataAnalyzer()

    analyzer.get_file() 
    questions = analyzer.get_queries()
    for i,q in enumerate(questions):
        # 生成代码
        code = analyzer.generate_code(q)
        with open(f'outcome/code_{i}.py','w') as f:
            f.write(code)
        result = analyzer.execute_code(code)
        # 错误处理
        count=0
        while result['status'] == 'error' and count<3:
            count+=1
            code = analyzer.debug_code(result,q,code)
            result = analyzer.execute_code(code)
        if result['status'] == 'error':
            print(f"代码执行出错: {result['message']}")
            continue
        with open(f"outcome/result_{i}.pkl",'wb') as f:
            pickle.dump(result['outcome'],f)
        explanation ,histroy = get_chat_completion(success_prompt.format(query=q,outcome=str(result['outcome'])),analyzer.history)
        analyzer.history = histroy
        print("*"*20)
        print(f'{q}\n回答如下：\n{explanation}')
        with open(f"outcome/explanation_{i}.txt",'w') as f:
            f.write(explanation)
        print("*"*20)

if __name__ == "__main__":
    main()