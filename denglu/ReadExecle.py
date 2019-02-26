# coidng=utf-8
import xlrd,requests,json

class openExecle():
    def __init__(self,datapath,sheet):
        self.excefile = xlrd.open_workbook(datapath)
        self.sheet = self.excefile.sheet_by_name(sheet)
        self.nrows = self.sheet.nrows

    """ 获取参数 """
    def get_pram(self):
        listpram =[]
        for i in range(1,self.nrows):
            listpram.append(self.sheet.row(i)[6].value)
        return listpram

    """ 获取url """
    def get_url(self):
        listurl = []
        for i in range(1,self.nrows):
            listurl.append(self.sheet.row(i)[3].value)
        return listurl

    """ 获取请求方式 """
    def get_meth(self):
        listmeth = []
        for i in range(1,self.nrows):
            listmeth.append(self.sheet.row(i)[5].value)
        return listmeth

    """ 获取期望code """
    def get_code(self):
        listcode = []
        for i in range(1,self.nrows):
            listcode.append(self.sheet.row(i)[7].value)
        return listcode

    """ 获取msg """
    def get_msg(self):
        listmsg = []
        for i in range(1,self.nrows):
            listmsg.append(self.sheet.row(i)[8].value)
        return listmsg

    def get_id(self):
        listid=[]
        for i in range(1,self.nrows):
            listid.append(int(self.sheet.row(i)[0].value))
        return listid
    def get_name(self):
        listname=[]
        for i in range(1,self.nrows):
            listname.append(self.sheet.row(i)[1].value)
        return listname

if __name__ =="__main__":
    a = openExecle(r'.\Data\testcase.xlsx',u"test_denglu")
    print(a.nrows)






