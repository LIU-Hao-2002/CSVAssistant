personal_base =  ''
personal_key = ""  
default_gpt_model = ""
exception_log_path="exception.log"
max_try_num=2

generate_code_query = """
你是一个数据分析助手。当前数据集包含以下列：{columns}。我有一个新的请求：{query}。请生成Python代码（使用变量df）。

要求1：python代码必须严格按照markdown格式，包括代码块和注释。即：
```python
# 你的代码
```
要求2：写完代码后，请接着生成一部分自然语言解释，解释代码的作用，不能直接结束你的回复。


"""

error_prompt = """你写的代码执行出错了。错误信息: {error}。请根据我的请求{query}修正以下代码：{code}
要求1：python代码必须严格按照markdown格式，包括代码块和注释。即：
```python
# 你的代码
```
要求2：写完代码后，请接着生成一部分自然语言解释，解释代码的作用，不能直接结束你的回复。
"""

success_prompt = """
关于请求{query}，你的代码执行成功了。以下是代码的执行结果：{outcome}。
请你基于结果中的数据，结合请求所问的具体问题，生成一部分自然语言解释，解释结果的含义，回答这个请求，务必详实。
"""
