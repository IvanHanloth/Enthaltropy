# Entrothalpy 熵焓杂病论
An calculator of the enthalpy, entropy and Gibbs free energy of chemical equation.

一个用于计算化学反应熵、焓、自由能变化的计算器，专门用于解决熵焓杂病
## How to use 如何使用
### Not Developer 非开发者
**Use Built Version 使用封装完成的版本**

1. Visit [Releases Page](https://github.com/IvanHanloth/Entrothalpy/releases) and download the latest release package and unzip  访问[Releases Page](https://github.com/IvanHanloth/Entrothalpy/releases)，下载最新版的压缩包并解压

2. Run main-en.exe.The console will be poped up and print introduction automatically  运行main-cn.exe，之后终端将自动弹出并输出简介

3. Follow the steps, input the temparature(K) and press Enter to continue. Or press Enter directly to set it at 298K 按照步骤，输入反应温度（K）并回车继续后续步骤。或直接按回车键，将其设置为298K

4. Input the reactant's formula, state, coefficient in order. When finish one, it will automatically start to ask for another chemical's information. If you've finished input all the reactants' information, press Enter when it is asking for the formula again and it will stop asking for reactant and move on to the products part.按顺序输入反应物的化学式、状态、系数。每完成一个反应物信息的输入，程序将自动询问另一个反应物的信息。当你完成了所有反应物信息的输入，在程序再次询问化学式时按下回车，它会停止询问反应物，并开始进入产物部分。

5. Repeat similar steps for products and when finish all the parts, it will print a complete equation in the console. Please check the correctness. If it's true, press Enter to calculate and if not, input any character and press Enter, it will ask you to reinput the information.  对产物部分重复相同的步骤。完成所有部分后，程序将自动输出一个完整的化学方程式。请检查方程是否正确，若正确，则按下回车进行计算，若有误，则输入任意字符并回车，程序将重新询问反应信息。

### Developer 开发者
**Run with Python 使用Python直接运行**
1. Download source code or `git clone` the repository.  下载源代码或执行`git clone`克隆仓库
2. Check the environment. It's recommanded to use Python 3.10+.  检查环境。推荐运行环境为Python3.10+
Install `openpyxl` moudle with `pip install openpyxl`. 使用`pip install openpyxl`命令，安装`openpyxl`模块
3. Run `main-en.py` with Python and follow the steps above to use it. 使用Python运行`main-cn.py`，并按照上面的步骤使用它

## Tips 提示

To use the tool to search the data of the chemical, please follow the rules below to input the chemical formula:

使用该工具搜索化学物质数据，请按照以下规则输入化学式：

1. The chemical formula should be in the correct case, such as H2O, not h2o.   严格大小写，如H2O，不可写成h2o

2. All subscripts and superscripts are entered directly as numbers, with subscripts before superscripts, such as the tetraammine copper ion is Cu(NH3)42+.  所有上下标直接输入数字，先下标后上标，如四氨合铜离子为Cu(NH3)42+
3. All hydrates are written with a space instead of a dot, such as the hydrate of copper sulfate is CuSO4 5H2O.  所有水合物的点写为空格，如硫酸铜的水合物为CuSO4 5H2O

## Further Develop 继续开发
Programme use the data from `data.xlsx` to query the information of chemicals. Therefore, you can add the chemical data by yourself to complete it.  程序使用`data.xlsx`中的数据来查询化学物质的相关信息。因此，你可以自己添加化学物质的信息来完善程序。

Insert new lines as bellow. The formula should follow the tips above and notice the unit of data

| Formula | State(s/g/l/aq/...) | H(KJ/mol) | S(J/mol) | G(KJ/mol)|
| :----: | :----: | :----: | :---: |:---:|
| Na | s | ... | ... | ... |

按照下面的格式插入新的行。其中化学式需要遵循上面的提示，并且注意数据的单位

| 化学式 | 状态(s/g/l/aq/...) | 焓(KJ/mol) | 熵(J/mol) | 自由能(KJ/mol)|
| :----: | :----: | :----: | :---: |:---:|
| Na | s | ... | ... | ... |

You can commit and push your change to the repository to make the data complete for everyone.  你可以提交并推送你的更改到仓库，来使大家的数据更加完整。

