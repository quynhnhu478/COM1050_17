def fibonacci_recursive(n):
   if n == 0:
       return [0]
   elif n == 1:
       return [1]
   elif n == 2:
       return [0, 1]
   else:
       seq = fibonacci_recursive(n-1)
       seq.append(seq[-1] + seq[-2])
       return seq
n = int(input())
print(1+sum(fibonacci_recursive(n-1)))