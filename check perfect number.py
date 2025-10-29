print("perfect number:")
def is_perfect(n):
    if n<=1:
        return False
    sum_of_divisions=1
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            sum_of_digits+=i
            if i !=n//i:
                sum_of_divisions+=n//i
        return sum_of_divisions==n
n=int(input("enter a number:"))
if is_perfect(n):
    print(f"{n}is a perfect number:")
else:
    print(f"{n} is not perfect number:")
