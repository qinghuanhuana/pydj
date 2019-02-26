#coding = utf-8
# a = 13666666666
#
# with open("mobile.txt","w") as fp:
#     for i in range(1,10001):
#         a+=1
#         fp.write(str(a)+"\n")
#
# import os
# a = os.getcwd()
# b = os.path.dirname(os.path.realpath(__file__))
# c = os.path.dirname(os.path.dirname(__file__))
# print(a+'\n'+b,c)

from denglu.ReadExecle import openExecle

class open(openExecle):
    def oen(self):
        listname=[]
        for i in range(0,self.nrows):
            listname.append(self.sheet.row(i)[0].value)
        return listname
a = open('C:\\Users\\ASUS\\Desktop\\3.7.4遗留问题解答.xlsx','Sheet3')
b= a.oen()
print(b)
