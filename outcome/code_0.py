
import pandas as pd
import matplotlib.pyplot as plt

# 假设 df 是已经加载的数据集
# 过滤出 Clothing 类别的数据
clothing_data = df[df['Category'] == 'Clothing']

# 按年份汇总销售额
sales_trend = clothing_data.groupby('Year')['Sales'].sum().reset_index()

# 绘制销售额趋势图
plt.figure(figsize=(10, 6))
plt.plot(sales_trend['Year'], sales_trend['Sales'], marker='o')
plt.title('Clothing Sales Trend Over Time')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.grid()
plt.xticks(sales_trend['Year'], rotation=45)
plt.tight_layout()
plt.show()
