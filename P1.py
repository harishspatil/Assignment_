#Python program to get the Fibonacci series between 0 to 50
a = 0
b = 1
for n in range(0, 10):
           if(n <= 1):
                      c = n
           else:
                      c = a + b
                      a = b
                      b = c
           print(c)