#檔案名稱：day16_2
#練習使用idle除錯

for x in range(5):
    print(x)

num = [1,2,3,4,5]
y = iter(num)
tt = iter(range(5))
#這邊會出現錯誤，試著修正。
print (tt.next())
