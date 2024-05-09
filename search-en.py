import openpyxl

workbook = openpyxl.load_workbook('data.xlsx')

sheet = workbook.active
print("""To use the tool to search the data of the chemical, please follow the rules below to input the chemical formula:
1. The chemical formula should be in the correct case, such as H2O, not h2o
2. All subscripts and superscripts are entered directly as numbers, with subscripts before superscripts, such as the tetraammine copper ion is Cu(NH3)42+
3. All hydrates are written with a space instead of a dot, such as the hydrate of copper sulfate is CuSO4 5H2O
""")
formula=input("The formula of the chemical:")
state=input('The state of the chemical(g/l/s/aq):')
data=None
for row in sheet.iter_rows(values_only=True):
    if row[0]==formula and row[1].upper()==state.upper():
        data=row
        break
if data:
    print(f"The enthalpy of {data[0]}({data[1]})is {data[2]}KJ/Mol, and the entropy is {data[3]}J/Mol, Gibbs free energy is{data[4]}KJ/Mol")
else:
    print("Can not found the data.")

workbook.close()