# coidng=utf-8
import xlrd
import json

class openExecle(object):
    def __init__(self, excelPath, sheet):
        self.excefile = xlrd.open_workbook(excelPath)
        self.sheet = self.excefile.sheet_by_name(sheet)
        self.nrows = self.sheet.nrows     #总行数
        self.ncols = self.sheet.ncols     #总列数

    """ 获取参数 """
    def get_pram(self):
        listpram =[]
        for i in range(0, self.nrows):
            listpram.append(self.sheet.row(i)[6].value)
        return listpram

    """ 获取url """
    def get_url(self):
        listurl = []
        for i in range(0, self.nrows):
            listurl.append(self.sheet.row(i)[3].value)
        return listurl

    def get_url2(self):
        listurl2 = []
        for i in range(0, self.nrows):
            listurl2.append(self.sheet.row(i)[4].value)
        return listurl2

    """ 获取请求方式 """
    def get_meth(self):
        listmeth = []
        for i in range(0, self.nrows):
            listmeth.append(self.sheet.row(i)[5].value)
        return listmeth

    """ 获取期望code """
    def get_code(self):
        listcode = []
        for i in range(0, self.nrows):
            listcode.append(self.sheet.row(i)[7].value)
        return listcode

    """ 获取msg """
    def get_msg(self):
        listmsg = []
        for i in range(0, self.nrows):
            listmsg.append(self.sheet.row(i)[8].value)
        return listmsg

    def get_id(self):
        listid=[]
        for i in range(0, self.nrows):
            listid.append(int(self.sheet.row(i)[0].value))
        return listid

    def get_name(self):
        listname=[]
        for i in range(0, self.nrows):
            listname.append(self.sheet.row(i)[1].value)
        return listname

if __name__ =="__main__":
    a = openExecle(r'.\Data\tacase.xlsx', "test_denglu")
    str1 = a.get_url()[1]
    str2 = a.get_url2()[1]
    print(str1+str2)






