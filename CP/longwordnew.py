n = int(input())

def my_function(n):
    for i in range(n):
        a = input()
        if len(a)>10:
            b = len(a[1:-1])
            print(f'{a[0]}{b}{a[-1]}')
        else:
            print(a)
        
my_function(n)