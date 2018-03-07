
from math import sqrt

#itentifiers all square numbers that can be create by adding 3 smaller square numbers
#equation based of (a^2 + b^2 + (a+b as 'c')^2) = square rootable number
for num1 in range (1, 101, 1):  
    num1sq = num1 * num1    

    for num2 in range (num1, 101,1):   
        num2sq = num2 * num2
        num3 = num1 * num2
        num3sq = num3 * num3

        total = (num1sq + num2sq + num3sq)
        root = sqrt(total)

        if (root % 1 == 0):
            print(num1, num2 ,num3, root)

