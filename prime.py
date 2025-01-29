print("PRIME NUMBERS BETWEEN 1 AND 100: \n")
for x in range(2,100+1):
    if all(x%i!=0 for i in range(2,int(x**0.5)+1)):
        print(x)

