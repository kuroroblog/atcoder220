# 標準入力を受け付ける。
N = int(input())

A = list(map(int, input().split()))

X = int(input())

# Aの配列を合算する。
ASum = sum(A)

# XはAの配列を合算したものを、何個ぶん持てるのか演算する。(はじめの項(A0)から足し合わせて、制約違反するのを防ぐため。)
cnt = X // ASum

# Aiのはじめの項(A0)からXを超えているのか検証するのではなく、(Xが持つことのできる、Aの配列を合算したものの個数) x (Aの配列を合算したもの)から検証を始める。
AiList = cnt * ASum
remainCnt = 0
for i in range(len(A)):
    # Xを超えたら検証を終了する。
    if AiList > X:
        break
    # Ai項を足し合わせる。(Xを超えるか検証を続けるため。)
    AiList += A[i]
    # Xを超えるために費やした、残りの項数を数える。
    remainCnt += 1

print(cnt * len(A) + remainCnt)
