
import pandas as pd
import matplotlib.pyplot as plt

# 假设 df 是已经加载的数据集
# 过滤出 Bikes 类别的数据
bikes_data = df[df['Category'] == 'Bikes']

# 按年份汇总销售额
sales_trend_bikes = bikes_data.groupby('Year')['Sales'].sum().reset_index()

# 绘制销售额趋势图
plt.figure(figsize=(10, 6))
plt.plot(sales_trend_bikes['Year'], sales_trend_bikes['Sales'], marker='o')
plt.title('Bikes Sales Trend Over Time')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.grid()
plt.xticks(sales_trend_bikes['Year'], rotation=45)
plt.tight_layout()
plt.show()
