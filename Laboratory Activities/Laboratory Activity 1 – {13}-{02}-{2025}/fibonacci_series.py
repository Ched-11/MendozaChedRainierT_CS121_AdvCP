number = int(input("Enter the number of terms : "))

first = 0
second = 1

print("Fibonacci Series: ", first, second, end=" ")
for _ in range (2,number):
    next_term = first + second
    print(next_term, end= " ")
    first = second
    second = next_term

