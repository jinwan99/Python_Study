def myfunc(param1,param2,param3):
    return f'param1:{param1},param2:{param2},param3:{param3}'

# 【アンパック】処理を行う
print(myfunc(*'abc'))
print(myfunc(1,*'23'))
print(myfunc(*'12',3))