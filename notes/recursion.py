# JS, 1st, Recursion Notes

# ------------------------------------

# normal loop
#for num in range(1, 11):
#    if num % 2 == 0:
#        print(num)

# ------------------------------------

#num = 9999; sum = 1

# ------------------------------------

#for x in range(1, num + 1):
#    sum *= x
#print(f"Loop: {sum}")

#def factorial(n):
#    if n == 1: return 1
#    return n * factorial(n-1)

#print(f"Recursion: {factorial(num)}")

# ------------------------------------

fibonacci = [1, 1]

for i in range(1, 11):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i])

print(f"Loop: {fibonacci}")

def fib_next(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fib_next(n-1) + fib_next(n-2)

print(f"Recursion: {fib_next(11)}")