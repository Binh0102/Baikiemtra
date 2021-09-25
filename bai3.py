while True:
    try:
        n = int(input("Nhap số nguyên dương: "))
        break
    except:
        print("Không phải số nguyên dương vui lòng nhập lại!")
        continue
def giaithua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua
print("Giai thừa của n là",giaithua(n))