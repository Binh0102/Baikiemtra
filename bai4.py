n=int(input("Nhập một số nguyên dương:"))
def tongcacchuso(n):
    phantu = 0
    while (n > 0):
        phantu = phantu + n % 10
        n = int(n / 10)
    return phantu
print("Tổng cac chữ số là:",tongcacchuso(n))