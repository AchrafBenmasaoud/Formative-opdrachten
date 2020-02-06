'''
Naam= Achraf_Benmasaoud
Studentennummer= 1761787
Klas= V1A
Datum= 6-2-2020
'''

#opdracht 1
x = int(input('Hoe groot'))
for x in range(1, x+1):
    print('*' * x)

for x in range(4,0,-1):
    print('*'*x)
i = 0
y= '*'
while i <= x:
    b = i * y
    i+=1
    print(b)
while x > 0:
     p = x * y
     x= x -1
     print(p)

#opdracht 2
def check():
    n= str(input(' Geef een string:'))
    p= str(input(' Geef een string:'))
    for index in range(len(n)):
        if n[index] != p[index]:
            print('Het eerste verschil zit op index:' + str([index]))
            break
        else:
            print('Geen verschil')
        # samen met Berke samengewerkt
check()

#opdracht 3.A
def count():
    n=([2,3,4,5,6,7,9])
    for x in n:
        p= n.count(x)                   # hier komt dan je getal die wil weten
        print('Dit getal komt zovaak voor:',p)
count()

# opdracht 3.B
def difference():
    test_list2=[]
    test_list=[2,3,4,5,6,2,3]
    difference = [j - i for i, j in zip(test_list[: -1], test_list[1:])]
    for x in difference:
        test=abs(x)
        test_list2.append(negatief)
    print(max(test_list2))
difference()
# Samen met berke
# https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/

#opdracht 3.C
def check2():
    n = ([1,1,1,0,0])
    for x in n:
        p = n.count(x)
        print('Dit getal komt zovaak voor:',p)

# hier kwam ik niet echt uit, hoop dat ik met de feedback dit kan verbeteren

#opdracht 4
def palindroom():
    n = str(input('Welke woord moet ik checken voor je: '))
    if(n == (n[:: -1])):
        print('Dit is een palindroom want: ' + n + ' = ' + n [::-1])
    elif(n!=(n[:: -1])):
        print('Dit is geen palindroom want: ' + n + ' = ' + n [::-1])
    else:
        print('Dit is een incorrecte waarde')
palindroom()

#https://www.tutorialgateway.org/python-program-to-check-a-given-string-is-palindrome/

# opdracht 5
def sort():
    p=[5,6,7,7,8,8,3,2,1]
    for i in range(len(p)):
        for x in range(i + 1, len(p)):
            if p[i] > p[x]:
                p[i], p[x] = p[x], p[i]
    print(p)
sort()
# https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function

#opdracht 6
def gemiddelde():
    summer = 0
    counter = 0
    lst = [6, 5, 9, 7, 8, 7]
    for x in lst:
        summer = summer + x
        counter = counter + 1
    b = summer / counter
    print(b)
gemiddelde()

#opdracht 7
def quess():
    import random
    n=int(input('Raad het getal: '))
    d=random.randrange(0,7)
    while True:
        if d == n:
            print('Je bent een ster!')
            break
        elif d != n:
            quess()
            break
quess()

#opdracht 8
def compressie():
    file=open('test.txt', 'r')
    for line in file:
        lines = line.strip()
        if lines:
            print(lines)
compressie()

# samen met Berke samengewerkt

# https://stackoverflow.com/questions/10794245/removing-spaces-and-empty-lines-from-a-file-using-python/10794299

#opdracht 9
# def cyclisch(ch, n):

# ik wist niet hoe ik deze moest aanpakken hopelijk door dmv feedback het op te lossen.

# opdracht 10
def feb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return feb(n-1)+feb(n-2)
input1=int(input('Geef een getal:'))
print(feb(input1))

# https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/
# https://nl.wikipedia.org/wiki/Rij_van_Fibonacci meer om te kijken wat het eigenlijk is


#opdracht 11
input1 = input('Geef een text: ')
input2 = int(input('Geef een rotatie: '))
def caesarcijfers(n,p):
  tekst = ' '
  for x in n:
    if x.isalpha():
      alphabet = ord(x) + p
    elif alphabet > ord('z'):
        alphabet -= 26
    letter = chr(alphabet)
    tekst += letter
    print ('Ceasarcode: ', tekst)
caesarcijfers(input1,input2)

# ik vond dit een lastige opdracht, ipv dat hij in 1x de ceasercode geeft, doet hij het op oplodend stukje creativiteit.
#https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python

# opdracht 12

def FizzBuzz():
    for Fizzbuzz in range(1,101,1):
        if Fizzbuzz % 3 == 0 and Fizzbuzz % 5 == 0:
            print('fizzbuzz')
            continue
        elif Fizzbuzz % 3 == 0:
            print('fizz')
        elif Fizzbuzz % 5 == 0:
            print('buzz')
        else:
            print(Fizzbuzz)
FizzBuzz()

# ik heb met Berke, Oualid en Adam samengewerkt aan de formative opdracht.
