harga = {"standar 30s" : int(65000),
         "xxl 30s" : int(70000), 
         "xxxl 30s" : int(75000), 
         "standar 24s" : int(67000), 
         "xxl 24s" : int(72000), 
         "xxxl 24s" : int(77000), 
         "warna" : int(2000), 
         "plastisol" : int(2500)
         }

def main():
    while True:
        try:
            print("\n============== Simulasi Pemesanan Sablon Kaos ==============")
            print()

            jumka = int(input("Masukkan jumlah kaos                             :"))

            uks = int(input("Masukkan jumlah kaos ukuran S                    :"))
            ukm = int(input("Masukkan jumlah kaos ukuran M                    :"))
            ukl = int(input("Masukkan jumlah kaos ukuran L                    :"))
            ukxl = int(input("Masukkan jumlah kaos ukuran XL                   :"))
            ukxxl = int(input("Masukkan jumlah kaos ukuran XXL                  :"))
            ukxxxl = int(input("Masukkan jumlah kaos ukuran XXXL                 :"))

            jwdes = int(input("Masukkan jumlah warna desain (Minimal 3 warna)   :"))
            jenka = str(input("Masukkan Jenis Bahan Kaos (30s/24s)              :"))
            jensa = str(input("Masukkan jenis sablon kaos (rubber/plastisol)    :"))

            perhitungan1 = ((harga["standar 30s"]+(harga["warna"]*(jwdes-2)))*(uks+ukm+ukl+ukxl))+((harga["xxl 30s"]+(harga["warna"]*(jwdes-2)))*ukxxl)+((harga["xxxl 30s"]+(harga["warna"]*(jwdes-2)))*ukxxxl)
            perhitungan2 = ((harga["standar 24s"]+(harga["warna"]*(jwdes-2)))*(uks+ukm+ukl+ukxl))+((harga["xxl 24s"]+(harga["warna"]*(jwdes-2)))*ukxxl)+((harga["xxxl 24s"]+(harga["warna"]*(jwdes-2)))*ukxxxl)
            perhitungan3 = (((harga["standar 30s"]+harga["plastisol"])+(harga["warna"]*(jwdes-2)))*(uks+ukm+ukl+ukxl))+(((harga["xxl 30s"]+harga["plastisol"])+(harga["warna"]*(jwdes-2)))*ukxxl)+(((harga["xxxl 30s"]+harga["plastisol"])+(harga["warna"]*(jwdes-2)))*ukxxxl)
            perhitungan4 = (((harga["standar 24s"]+harga["plastisol"])+(harga["warna"]*(jwdes-2)))*(uks+ukm+ukl+ukxl))+(((harga["xxl 24s"]+harga["plastisol"])+(harga["warna"]*(jwdes-2)))*ukxxl)+(((harga["xxxl 24s"]+harga["plastisol"])+(harga["warna"]*(jwdes-2)))*ukxxxl)
        except ValueError:
            print("\nXXXXXXXXXXXXXXXX Input salah format XXXXXXXXXXXXXXXX")
            print()
            continue

        if jumka == uks+ukm+ukl+ukxl+ukxxl+ukxxxl:
            if jwdes >= 3:
                if jenka.lower() == "30s" and jensa.lower() == "rubber":
                    print("\n============== Hasil Estimasi Biaya Pemesanan ==============")
                    print("\nRp.",perhitungan1)
                    print()
                    break
                elif jenka.lower() == "30s" and jensa.lower() == "plastisol":
                    print("\n============== Hasil Estimasi Biaya Pemesanan ==============")
                    print("\nRp.",perhitungan3)
                    print()
                    break
                elif jenka.lower() == "24s" and jensa.lower() == "rubber":
                    print("\n============== Hasil Estimasi Biaya Pemesanan ==============")
                    print("\nRp.",perhitungan2)
                    print()
                    break
                elif jenka.lower() == "24s" and jensa.lower() == "plastisol":
                    print("\n============== Hasil Estimasi Biaya Pemesanan ==============")
                    print("\nRp.",perhitungan4)
                    print()
                    break
                else:
                    print("\nXXXXXXXXXXXX Salah input!!! XXXXXXXXXXXX")
                    print()
                    continue
            else:
                print("\nXXXXXXX Jumlah warna desain kaos tidak valid XXXXXXX")
                print()
                continue
        else:
            print("\nXXXX Jumlah kaos dengan jumlah ukuran kaos tidak sama XXXX")
            print()
            continue

main()    