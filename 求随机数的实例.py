"""
求一个0~255的随机数
"""


import random
ret = random.randint(0, 255)
print(ret)


# 如何生成五位数的字母和数字随机组合的验证码, "A3bv7"
tmp_list = []
for i in range(5):
    u = chr(random.randint(65, 90))  # 生成大写字母
    l = chr(random.randint(97, 122))  # 生成小写字母
    n = str(random.randint(0, 9))  # 生成数字，注意要转换成字符串类型
    # print(u,l,n)
    tmp = random.choice([u, l, n])
    print(tmp)
    tmp_list.append(tmp)
print(tmp_list)
print("".join(tmp_list))
list1 =  "".join(tmp_list)
print(list1)
