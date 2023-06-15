n = (int(input()))
sum1, sum2=0, 0
for i in range(0, n+1):
    sum1+=i**2
    sum2+=i
print(sum2**2-sum1)