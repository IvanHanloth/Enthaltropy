import openpyxl

workbook = openpyxl.load_workbook('data.xlsx')

sheet = workbook.active
print("""使用该工具搜索化学物质数据，请按照以下规则输入化学式：
1.严格大小写，如H2O，不可写成h2o
2.所有上下标直接输入数字，先下标后上标，如四氨合铜离子为Cu(NH3)42+
3.所有水合物的点写为空格，如硫酸铜的水合物为CuSO4 5H2O
""")
formula=input("输入物质化学式：")
state=input('输入物质状态(g/s/aq/l)：')
data=None
for row in sheet.iter_rows(values_only=True):
    if row[0]==formula and row[1].upper()==state.upper():
        data=row
        break
if data:
    print(f"{data[0]}（{data[1]}）的焓为{data[2]}KJ/Mol,熵为{data[3]}J/Mol,自由能为{data[4]}KJ/Mol")
else:
    print("未找到数据")

workbook.close()