# coding=utf-8

# def add_num(num):
#     with open('%s.txt'%num, 'w') as fp:
#         for i in range(1,100):
#             num += 1
#             fp.write(str(num) + '\n')
#
# add_num(49110000)
import os

def File_num(path):
    if os.path.isfile(path):
        print('file num is 1')
        return
    num = 0
    file_num = 0
    for i in os.listdir(path):
        file_path = os.path.join(path, i)
        if os.path.isfile(file_path):
            num += 1
            print(file_path)
        else:
            file_num += 1
            File_num(file_path)
    print('文件：%s' % num, '文件夹：%s' % file_num, '路径：%s' % (path))

def listto(insert_list):
    if type(insert_list) == list:
        if len(insert_list) == 1:
            if type(insert_list[0]) is not int:
                return False
            return insert_list
        for item in insert_list:
            try:
                if item % 2 == 0:
                    insert_list.remove(item)
                    insert_list.insert(0, item)
            except:
                return False
        return insert_list
    else:
        return False


if __name__ == "__main__":
    # File_num('F:\\GitHub\\lexin')
    a = listto([1, 2, 4, '5'])
    print(len([1, 2, 4, '5']))



