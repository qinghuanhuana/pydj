# coidng=utf-8
import yaml,os
#当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))

#yaml文件路径
yamlpath = os.path.join(basepath, 'pageelement')

def parseyaml():
    pageElements = {}
    '''每次遍历的对象都是返回的是一个三元组(root,dirs,files)
root 所指的是当前正在遍历的这个文件夹的本身的地址
dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
'''
    for fpath,dirname,fnames in os.walk(yamlpath):
        for name in fnames:
            yaml_file_path = os.path.join(fpath,name)
            if '.yaml' in str(yaml_file_path):
                with open(yaml_file_path,'r',encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElements.update(page)
    return pageElements

def LonginPage():
    a = parseyaml()
    list = []
    for i in a['LonginPage']['locators']:
        list.append(i)
    return list

def MinePage():
    a = parseyaml()
    list = []
    for i in a['MinePage']['locators']:
        list.append(i)
    return list

def ZhucePage():
    a = parseyaml()
    list = []
    for i in a['ZhucePage']['locators']:
        list.append(i)
    return list

def ShouyePage():
    a = parseyaml()
    list = []
    for i in a['ShouyePage']['locators']:
        list.append(i)
    return list


if __name__ == "__main__":
    b = MinePage()
    login_loc = (b[8]['type'], b[8]['value'])
    print (login_loc)
