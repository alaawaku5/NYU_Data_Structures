# Question 4 a:
print([10 ** i for i in range(6)])

# Question 4 b:
print([i * (i + 1) for i in range(10)])

# Question 4 c:
lst = []
[lst.append(chr(i + ord('a'))) for i in range(26)]
print(lst)
