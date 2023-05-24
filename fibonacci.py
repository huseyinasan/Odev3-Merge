print("Fibonacci Hesaplama")

a = 1
b = 1
fibonacci = [a, b]

n = int(input("Kaçıncı Fibonacci sayısını görmek istiyorsunuz?"))

for i in range(2, n):
    a, b = b, a + b
    fibonacci.append(b)
print(fibonacci)




    