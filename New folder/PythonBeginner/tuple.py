'''''
#syntax

tp = 1,2,3,4.5,"bill",False

print(type(tp))
print(tp[1],tp[-1],tp[2],sep="|")#access

#iteration

for i in tp:
    print(i)


#comparison

tp1 = 11,2,3,4,6
tp2  =11,2,3,4,6
tp3 = 11,2,3,4,6

if tp1 ==tp2 == tp3:
    print("t1 and t2 values are equal")'''

#immutable

tp1 = 11,2,3

print(tp1)

#unpacking or multiple assignment

x,y,z=tp1

print(x,y,z,sep=" | ")

a,b,_=tp1
print(a,b,_,sep=" | ")




