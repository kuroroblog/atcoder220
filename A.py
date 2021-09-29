# 標準入力を受け付ける。
A, B, C = map(int, input().split())

# A以上B以下の倍数が見つかるかどうかのflagを用意する。flagをFalseにしておく。
flag = False
# A以上B以下の倍数が見つかるまで、while文を回す。
while True:
    # A以上B以下の倍数が見つかったら、flagをTrueにし、while文をbreakする。
    if A <= C and B >= C:
        flag = True
        break

    # B < Cになったら、while文をbreakする。(検証終了のため)
    if B < C:
        break

    # A以上B以下の倍数が見つかるまで、C = C + Cを繰り返す。(次のCの倍数の値がA以上B以下に含まれるか、確認するため。)
    C += C

# flagがTrueのとき、現在のCの値を出力する。flagがFalseのとき、-1を出力する。
if flag:
    print(C)
else:
    print(-1)
