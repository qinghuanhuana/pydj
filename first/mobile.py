#coding = utf-8

#
# import os
# a = os.getcwd()
# b = os.path.dirname(os.path.realpath(__file__))
# c = os.path.dirname(os.path.dirname(__file__))
# print(a+'\n'+b,c)

from denglu.ReadExecle import openExecle

class open(openExecle):
    def oen(self):
        listname = []
        listmodel = []
        for i in range(0, self.nrows):
            listname.append(self.sheet.row(i)[0].value)
            listmodel.append(self.sheet.row(i)[1].value)
        return listname, listmodel



if __name__ == "__main__":
    a = open('C:\\Users\\ASUS\\Desktop\\手机借用记录.xls', 'Sheet1')
    b = a.add_num(441100)
    print(b)
