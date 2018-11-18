#质数问题代码
x=1
while x==1:
    n=int(input("请输入一个大于一的整数并以'-1'结束："))#获取一个数
    if n==-1:
       break
    else:
        zs=[]
        for i in range(2,n):
            for j in range(2,i):
                if (i%j==0):
                    break
            else :
                    zs.append(i)
        print (f"小于{n}的质数为{zs}")
