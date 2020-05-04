"""set1 = set()
set2 = set()

n1 = int(input())
for i in range(n1):
    num1 = int(input())
    set1.add(num1)
n2 = int(input())
for j in range(n2):
    num2 =int(input())
    set2.add(num2)

n=set1 - set2
print(len(n))"""
"""def test():
    try:
        print(1)
    finally:
        print(2)
test()"""
"""if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    temp =  [ [ i, j,k] for i in range( x + 1) for j in range( y + 1) for k in range(z+1)if ( ( i + j + k) != n) ]
    print(temp)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])"""

nameer = []
scorer = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = str(input(""))
        score = float(input())
        nameer = nameer + [[name,score]]
        scorer = scorer + [score]
        scorer.sort()
    x = sorted((set(scorer)))[1]
    for nam,scor in sorted(nameer):
        if(scor == x):
            print(nam)
            
        
        




