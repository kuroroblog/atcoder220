# 標準入力を受け付ける。
K = int(input())

A, B = input().split()

# 参考 : https://science-log.com/python%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0tips%E9%9B%86/%E3%80%90python%E3%80%91%E8%A8%98%E6%95%B0%E6%B3%95%E3%81%AE%E5%A4%89%E6%8F%9B/
print(int(str(A), K) * int(str(B), K))
