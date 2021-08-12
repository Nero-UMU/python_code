def hanoi( n, X, Y, Z ):
    if n == 1:
        print (X, ' --> ', Z)
    else:
        hanoi(n - 1, X, Z, Y)
        print(X, ' --> ', Y)
        hanoi(n - 1, Y, X, Z)
        print(Y, ' --> ', Z)

print('请输入汉诺塔金片的数量：')
number = eval(input())
hanoi(number, 'X', 'Y', 'Z')
