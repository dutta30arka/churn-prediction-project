a = []
s = int(input("Enter the size of the list: "))

# Input the values and append to the list
for i in range(s):
    v = int(input("Enter value: "))
    a.append(v)

n=len(a)+1
a_s=sum(a)
ts=n*(n+1)//2
mn=ts-a_s
print(mn)
