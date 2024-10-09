saldo = 500000
lanjut_beli = "y"
user = {"username":"Danella" , "password":"oke1234"}
logged = "gagal"

def beli_pulsa(p):
    global saldo
    if saldo >=int(p):
        saldo -=int(p)
        print("Anda berhasil membeli pulsa Rp.",p)
        print("sisa saldo anda adalah Rp.",saldo)
    else:
        print("Ops saldo anda tidak cukup")

while logged == "gagal":
    print("Mau beli pulsa? silahkan log in")
    username = input("masukkan username : ")
    password = input("masukkan password : ")
    if username == user['username'] and password == user['password']:
        print("Selamat Datang"+user['username'])
        logged = "berhasil"
    else:
        print("Ops username/password anda salah")
    
while lanjut_beli =="y" and logged =="berhasil":
    print("Beli Pulsa")
    print("1.Beli Pulsa Rp.5.000")
    print("2.Beli Pulsa Rp.10.000")
    print("3.Beli Pulsa Rp.20.000")
    print("4.Beli Pulsa Custom")
    print("5.keluar aplikasi")
    a = int(input("Silahkan pilih pulsa yang mau dibeli : "))
    if a == 1:
        beli_pulsa(5000)
    elif a == 2:
        beli_pulsa(10000)
    elif a == 3:
        beli_pulsa(20000)
    elif a == 4:
        beli_pulsa(input("silahkan masukkan nominal pulsa yang akan diisi Rp."))
    elif a == 5:
        lanjut_beli = "n"
    else:
        print("pilihan tidak tersedia")
    lanjut_beli=input("mau isi lagi???(y/n)")
    


