def buat():
    ida=str(input("Masukkan nama file : "))
    file=open(f'{ida}',"w")
    nama=str(input("Masukkan Namamu : "))
    nim=str(input("Masukkan NIM kamu : "))
    angkatan=str(input("Masukkan tahun angkatanmu : "))
    file.write(f'Nama : {nama}\nNIM : {nim}\nAngkatan : {angkatan}')
    file.close()

def baca():
    ida=str(input("Masukkan nama file : "))
    file = open(f'{ida}', "r")
    text = file.read()
    print(text)
    file.close()

def tambah():
    ida=str(input("Masukkan nama file : "))
    file = open(f'{ida}', "a")
    hewan=str(input("Masukkan Hewan Favoritmu : "))
    catatan=str(input("Catatan tambahan : "))
    file.write(f'Hewan Favorit : {hewan}\nCatatan : {catatan}')
    file.close()

while True:
    print(f'====== Program file Handling ======\n1. Membuat dan membaca file\n2. Membaca file\n3. Menambahkan text pada file\n4. Keluar dari program')
    n = int(input("Masukkan nomor perintahmu : "))
    if (n == 1):
        print(f'\n{buat()}\n')
    elif (n==2):
        print(f'\n{baca()}\n')
    elif (n==3):
        print(f'\n{tambah()}\n')
    elif (n==4):
        print("Terimakasih telah menggunakan program ini")
        break
    else :
        print("Mohon input nomor yang sesuai\n")