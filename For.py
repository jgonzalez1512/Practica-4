
print ("For 1")

x = int(input("digita primer numero "))
y = int(input("digita segundo numero "))

if x > y :
	print("el primer numero " + str(x) + " es mayor al segundo " +str(y))
else:
    for i in range(x + 1, y):
        if x % 2 == 0:
        	print(f"{i} par")
        else:
        	print(f"{i} impar")