# 変数をセットする
N = int(input())
A = list(map(int, input().split()))
cnt = 0

# 配列の要素がすべてが偶数である限り、ループさせる
while all( x % 2 == 0 for x in A):
    A = [x / 2 for x in A]
    cnt = cnt + 1

print(cnt)