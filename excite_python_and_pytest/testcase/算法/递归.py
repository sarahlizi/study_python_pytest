def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1)+f(n-2)

def ff(n):
    if n==0:
        return 1
    else:
        return n*ff(n-1)

def fff(zige):
    data={1,2,3}
    if zige ==1:
        data[0]=111
    elif zige ==2:
        data[0]=222
    elif zige ==3:
        data[0]=333
    else:
        print("未找到对应的资格")
    return data


if __name__=="__main__":
    i=input("请输入您想要的数字：")
    a = f(int(i))
    print(a)
    # a = ff(int(i))
    # print(a)

