#coding=utf-8
def dijian(n):
    if n == 1:
        return 1
    return n*dijian(n-1)
a = dijian(8)
b = a*10
print(b)

# def fenjie(n,the_dict):
#     for key,value in n.items():
#         if isinstance(value,dict):
#             fenjie(value,the_dict)
#         else:
#             the_dict[key]=value
#     return the_dict
# r = {"a":"aa","b":"bb","c":{"d":"dd","e":"ee"}}
# the_dict = dict()
# print(fenjie(r,the_dict))
# the_str = '12,33,44'
# the_list = the_str.split(',')
# print (the_list)
# print(','.join(the_list))
# the_dict = {'a': 'aa', 'b': 'bb', 'd': 'dd', 'e': 'ee'}
#
# #迭代字典的key值和value值
# for key,value in the_dict.items():
#     print(key)
#     print(value)
# #迭代字典的key值
# for key1 in the_dict.keys():
#     print(key1)
#
# #迭代字典的value值
# for value1 in the_dict.values():
#     print(value1)

# def maopao(n):
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             if n[i].split(':')[1] < n[j].split(':')[1]:
#                 n[i],n[j]=n[j],n[i]
#     return n
# stu = ['张三:20','李四:70','王五:88','李六:40','王吉:55.5',]
# print (maopao(stu))
# def student_achie(A):
#     for i in range(len(A)):
#         key = i
#         for j in range(i+1,len(A)):
#             if A[key].split(':')[1] < A[j].split(':')[1]:
#                 key = j
#         A[key],A[j] = A[j],A[key]
#     return A
#
# #学生姓名及学生成绩
# stu = ['张三:20','李四:70','王五:88','李六:40','王吉:55.5',]
#
# print(student_achie(stu))
#计算学生总成绩
# def total_achie(A):
#     if len(A) == 1:
#         return float(A[0].split(':')[1])
#     return float(A.pop().split(':')[1]) + total_achie(A)
# #学生姓名及学生成绩
# stu = ['张三:20','李四:70','王五:88','李六:40','王吉:55.5',]
#
# print(total_achie(stu))
# def feibonaqi(n):
#     list1=[]
#     for i in range(n):
#         if i == 0:
#             list1.append(1)
#         elif i== 1:
#             list1.append(1)
#         else:
#             list1.append(list1[i-1]+list1[i-2])
#     return list1
# print(feibonaqi(1))
# class Solution:
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         result = [nums[0], max(nums[0], nums[1])]
#         for i in range(2, len(nums)):
#             result.append(max(nums[i] + result[i - 2], result[i-1]))
#             print(result)
#         return result[-1]



