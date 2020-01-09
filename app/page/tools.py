import os
import jinja2
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

def get_page_list(yamlpage):
    page_object = {}
    for page, names in yamlpage.items():
        loc_names = []
        locs = names['locators']
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object

def create_pages(page_list):
    basepath = os.path.dirname(os.path.abspath('__file__'))
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)
    templateVars = {
        'page_list': page_list
    }
    template = template_env.get_template('templetpage')
    with open(os.path.join(basepath, 'pages.py'), 'w', encoding='utf-8') as f:
        f.write(template.render(templateVars))

if __name__ == '__main__':
    b = parseyaml()
    c = get_page_list(b)
    create_pages(c)