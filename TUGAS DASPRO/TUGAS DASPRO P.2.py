print("------------------------------")
print("Nama: Keisya Sit Nafisa Andini")
print("NIM: 240116115")
print("------------------------------")

# Masukkan Jabatan & Password

while True:
    print("Halo, Selamat Datang di Mini Project DDP")
    jabatan = input("Masukkan jabatan: ")
    password = input("Masukkan password: ")
    if jabatan == "administrasi" and password == "999":
        print("Anda berhasil masuk")
        break
    else:
        print("Anda tidak berhasil masuk, Silahkan masukkan jabatan dan password anda dengan benar")
        if False:
            break

# Inputan

Nama = str(input("Masukkan nama: "))
gol = input("Golongan: ")
jam = int(input("Masukkan jumlah jam: "))
gaji = 500000
if gol == "1":
    upah =0.05*gaji;
elif gol == "2":
    upah =0.10*gaji;
elif gol == "3":
    upah =0.15*gaji;
else:
    print ("tidak ada golongan")

# Menghitung rumus
if jam >= 160:
    lembur = jam - 160
    rumus = 160 * upah + lembur * 30000
else:
    rumus = jam * upah

    print (rumus)