print("\n")
print(62 * "=")
print("\t\tSELAMAT DATANG DI ATM SIMPEL")
print(62 * "=")
print("PILIH OPTION : ")
print("1. CEK UANG")
print("2. AMBIL UANG")
print("3. TABUNG UANG")

option = int(input("Silahkan pilih option : "))
uang_anda = 300000

if option == 1:
    print(62 * "-")
    print(f"\t\tUang saya berjumlah Rp{uang_anda}")
elif option == 2:
    print(f"Uang saya berjumlah {uang_anda}, Ditarik berapa?")
    print("1. Rp50.000")
    print("2. Rp100.000")
    print("3. Rp200.000")
    print("4. Rp300.000")
    option2 = int(input("Option : "))
    if option2 == 1:
        hasil = uang_anda - 50000
        print(62 * "-")
        print(f"\t      Uang anda sekarang berjumlah {hasil}")
    elif option2 == 2:
        hasil = uang_anda - 100000
        print(62 * "-")
        print(f"\t      Uang anda sekarang berjumlah {hasil}")
    elif option2 == 3:
        hasil = uang_anda - 200000
        print(62 * "-")
        print(f"\t      Uang anda sekarang berjumlah {hasil}")
    elif option2 == 4:
        hasil = uang_anda - 300000
        print(62 * "-")
        print(f"\t      Uang anda sekarang berjumlah {hasil}")
    else:
        print(62 * "-")
        print("Angka yang anda masukkan salah, mohon ulangi lagi!")
elif option == 3:
    print(f"Uang saya berjumlah {uang_anda}, Simpan berapa?")
    option3 = int(input("Masukkan jumlah uang:"))
    hasil3 = uang_anda + option3
    print(62 * "-")
    print(f"\t   Jumlah uang anda saat ini adalah {hasil3}")
else:
    print("Nomor anda salah, mohon ulangi lagi!!!")

print(62 * "=")
print("\n")
