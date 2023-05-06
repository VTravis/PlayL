fruits = []

f = input('enter your fruit (not):')

while f != 'not':
    if f in fruits:
        print('this fruit in list')
    else:
        fruits.append(f)
    f = input('enter your fruit (not):')

print(fruits)
input()