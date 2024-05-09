import openpyxl

workbook = openpyxl.load_workbook('data.xlsx')

sheet = workbook.active
def inputdata(name):
    res=[]
    print(f"The following part belongs to{name}. Press Enter when inputing formula to continue")
    while True:
        formula=input(f"The formula of {name}(Press Enter to next part):\r\n")
        if formula=="":
            break
        state=input(f'The state of {name}(g/s/aq/l): \r\n')
        number=input(f'The coefficient of {name}(default is 1):\r\n')
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
            print(f"The enthalpy of {data[0]}({data[1]})is {data[2]}KJ/Mol, and the entropy is {data[3]}J/Mol, Gibbs free energy is{data[4]}KJ/Mol")
            i['H']=float(data[2])
            i['S']=float(data[3])
            i['G']=float(data[4])
        else:
            print(f"cannot find the data of {i['formula']}({i['state']})")
            i['H']=0
            i['S']=0
            i['G']=0
    return formulas
print('''The program is used to calculate the enthalpy change, entropy change, and free energy change of the reaction
All chemical formula inputs follow the rules below:
1. The chemical formula should be in the correct case, such as H2O, not h2o
2. All subscripts and superscripts are entered directly as numbers, with subscripts before superscripts, such as the tetraammine copper ion is Cu(NH3)42+
3. All hydrates are written with a space instead of a dot, such as the hydrate of copper sulfate is CuSO4 5H2O''')
T=input("Input the temperature(K), press Enter to use 298K(25℃):\r\n")
T=298 if T=="" else int(T)
while True:
    reactants=inputdata("reactants")
    products=inputdata("products")
    equation=""
    for i in reactants:
        equation+=f"{i['number']}{i['formula']}({i['state']})+" if i['number']!=1 else f"{i['formula']}({i['state']})+"
    equation=equation[:-1]+"->"
    for i in products:
        equation+=f"{i['number']}{i['formula']}({i['state']})+" if i['number']!=1 else f"{i['formula']}({i['state']})+"
    equation=equation[:-1]
    if input(f"-----------------\r\nPlease check the equation \r\n{equation}\r\n Press Enter if it's true. Input any other character to reinput\r\n")=="":break
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
print(f"-----------------\r\nEquation:{equation}\r\nEnthalpy:{H}KJ\r\nEntropy:{S}J\r\nFree Energy(Calculated with G=G(Products)-G(Reactants)):{G}KJ\r\nFree Energy(Calculated with G=H-ST){G2}KJ")

workbook.close()