"""
請寫一個程式，讀入兩個數字，並求出它們的和。
"""
a,b = map(int, input().split(" "))  # 讀取輸入 以空白格切分 並分別轉換成整數 存入變數中
print(a + b)