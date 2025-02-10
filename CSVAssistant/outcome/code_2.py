
import pandas as pd

# 假设 df 是已经加载的数据集
# 过滤出 Components 和 Accessories 类别的数据
components_data = df[df['Category'] == 'Components']
accessories_data = df[df['Category'] == 'Accessories']

# 按年份汇总销售额
components_sales = components_data.groupby('Year')['Sales'].sum().reset_index()
accessories_sales = accessories_data.groupby('Year')['Sales'].sum().reset_index()

# 合并两个数据集以便比较
merged_sales = pd.merge(components_sales, accessories_sales, on='Year', suffixes=('_Components', '_Accessories'))

# 找出哪些年份 Components 的销售额高于 Accessories
years_with_higher_components = merged_sales[merged_sales['Sales_Components'] > merged_sales['Sales_Accessories']]

# 输出结果
print(years_with_higher_components[['Year', 'Sales_Components', 'Sales_Accessories']])
