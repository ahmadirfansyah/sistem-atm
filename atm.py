# Memanggil modul JSON
import json
from pprint import pprint

# Memanggil file JSON
data_users = open("users.json")

# Mengurai data JSON
user = json.load(data_users)

# Mencetak isi data
pprint(user)

print("\n")
print(62 * "=")
print("\t\tSELAMAT DATANG DI ATM SIMPEL")
print(62 * "=")

no_rekening = input("Masukkan No Rekening : ")
found_user = False

for x in user:
    if x["no_rekening"] == no_rekening:
        found_user = True
        break

if no_rekening in x["no_rekening"]:
    pin = input("Masukkan No PIN : ")
    if pin == x["pin"]:

        def cek_saldo(saldo):
            print("")
            print(62 * "-")
            print(f"\t\tSaldo anda berjumlah Rp{saldo}")

        def tarik_tunai(saldo):
            print("tarik tunai")
            print(f"Saldo anda Rp{saldo}, Ditarik berapa?")
            print("1. Rp50.000")
            print("2. Rp100.000")
            print("3. Rp200.000")
            print("4. Rp300.000")
            option2 = int(input("Option : "))
            if option2 == 1:
                hasil = saldo - 50000
                print(62 * "-")
                print(f"\t      Uang anda sekarang berjumlah {hasil}")
            elif option2 == 2:
                hasil = saldo - 100000
                print(62 * "-")
                print(f"\t      Uang anda sekarang berjumlah {hasil}")
            elif option2 == 3:
                hasil = saldo - 200000
                print(62 * "-")
                print(f"\t      Uang anda sekarang berjumlah {hasil}")
            elif option2 == 4:
                hasil = saldo - 300000
                print(62 * "-")
                print(f"\t      Uang anda sekarang berjumlah {hasil}")
            else:
                print(62 * "-")
                print("Angka yang anda masukkan salah, mohon ulangi lagi!")

        def setor_tunai(saldo):
            print("setor tunai")

        while True:
            print("")
            print("Pilih Menu : ")
            print("1. Cek Saldo")
            print("2. Tarik tunai")
            print("3. Setor Tunai")
            print("4. Keluar")

            option = int(input("Masukkan Pilihan : "))
            saldo = int(x["saldo"])

            if option == 1:
                cek_saldo(saldo)
            elif option == 2:
                tarik_tunai(saldo)
            elif option == 3:
                setor_tunai(saldo)
            elif option == 4:
                break
            else:
                print("Nomor anda salah, mohon ulangi lagi!!!")

            print(62 * "-")
            print("\n")
