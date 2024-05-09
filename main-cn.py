import openpyxl

workbook = openpyxl.load_workbook('data.xlsx')

sheet = workbook.active
def inputdata(name):
    res=[]
    print(f"下面是{name}部分，输入化学式时输入回车可进入下一步")
    while True:
        formula=input(f"输入{name}物质化学式(回车进入下一步):\r\n")
        if formula=="":
            break
        state=input(f'输入{formula}的状态(g/s/aq/l): \r\n')
        number=input(f'输入{formula}的配平系数(留空默认为1):\r\n')
        if number=="":
            number=1
        else:
            number=int(number)
        res.append({'formula':formula,'state':state,'number':number})
    return res

def search(formula,state):
    data=None
    for row in sheet.iter_rows(values_only=True):
        if row[0]==formula and row[1].upper()==state.upper():
            data=row
            break
    return data

def searchs(formulas):
    for i in formulas:
        data=search(i['formula'],i['state'])
        if data:
            print(f"{data[0]}（{data[1]}）的焓为{data[2]}KJ/Mol,熵为{data[3]}J/Mol,自由能为{data[4]}KJ/Mol")
            i['H']=float(data[2])
            i['S']=float(data[3])
            i['G']=float(data[4])
        else:
            print(f"未找到{i['formula']}({i['state']})的数据")
            i['H']=0
            i['S']=0
            i['G']=0
    return formulas
print('''本程序用于计算反应的焓变、熵变、自由能变
所有化学式的输入遵循以下规则：
1.严格大小写，如H2O，不可写成h2o
2.所有上下标直接输入数字，先下标后上标，如四氨合铜离子为Cu(NH3)42+
3.所有水合物的点写为空格，如硫酸铜的水合物为CuSO4 5H2O''')
T=input("输入温度(K)，留空默认为298K(25摄氏度):\r\n")
T=298 if T=="" else int(T)
while True:
    reactants=inputdata("反应物")
    products=inputdata("生成物")
    equation=""
    for i in reactants:
        equation+=f"{i['number']}{i['formula']}({i['state']})+" if i['number']!=1 else f"{i['formula']}({i['state']})+"
    equation=equation[:-1]+"->"
    for i in products:
        equation+=f"{i['number']}{i['formula']}({i['state']})+" if i['number']!=1 else f"{i['formula']}({i['state']})+"
    equation=equation[:-1]
    if input(f"-----------------\r\n请确认方程式是否为\r\n{equation}\r\n是则输入回车，否则输入任意字符重新输入\r\n")=="":break
reactants=searchs(reactants)
products=searchs(products)

H=0
S=0
G=0
for i in products:
    H+=i['number']*i['H'] 
    S+=i['number']*i['S']
    G+=i['number']*i['G']
for i in reactants:
    H-=i['number']*i['H']
    S-=i['number']*i['S']
    G-=i['number']*i['G']
G2=H-T*S*0.001
print(f"-----------------\r\n方程式{equation}\r\n焓变为{H}KJ\r\n熵变为{S}J\r\n自由能变为{G}KJ（通过G=G（生成物）-G（反应物）计算）\r\n自由能变为{G2}KJ（通过G=H-ST计算）")

workbook.close()