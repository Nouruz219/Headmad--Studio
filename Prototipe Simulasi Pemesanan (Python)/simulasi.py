harga = {"standar 30s" : int(50000),
         "xxl 30s" : int(55000), 
         "xxxl 30s" : int(60000), 
         "standar 24s" : int(55000), 
         "xxl 24s" : int(60000), 
         "xxxl 24s" : int(65000), 
         "warna" : int(2000), 
         "plastisol" : int(5000)
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

            jwdes = int(input("Masukkan jumlah warna desain (Minimal 1 warna)   :"))
            jenka = str(input("Masukkan Jenis Bahan Kaos (30s/24s)              :"))
            jensa = str(input("Masukkan jenis sablon kaos (rubber/plastisol)    :"))

            perhitungan1 = ((harga["standar 30s"]+(harga["warna"]*(jwdes)))*(uks+ukm+ukl+ukxl))+((harga["xxl 30s"]+(harga["warna"]*(jwdes)))*ukxxl)+((harga["xxxl 30s"]+(harga["warna"]*(jwdes)))*ukxxxl)
            perhitungan2 = ((harga["standar 24s"]+(harga["warna"]*(jwdes)))*(uks+ukm+ukl+ukxl))+((harga["xxl 24s"]+(harga["warna"]*(jwdes)))*ukxxl)+((harga["xxxl 24s"]+(harga["warna"]*(jwdes)))*ukxxxl)
            perhitungan3 = (((harga["standar 30s"]+harga["plastisol"])+(harga["warna"]*(jwdes)))*(uks+ukm+ukl+ukxl))+(((harga["xxl 30s"]+harga["plastisol"])+(harga["warna"]*(jwdes)))*ukxxl)+(((harga["xxxl 30s"]+harga["plastisol"])+(harga["warna"]*(jwdes)))*ukxxxl)
            perhitungan4 = (((harga["standar 24s"]+harga["plastisol"])+(harga["warna"]*(jwdes)))*(uks+ukm+ukl+ukxl))+(((harga["xxl 24s"]+harga["plastisol"])+(harga["warna"]*(jwdes)))*ukxxl)+(((harga["xxxl 24s"]+harga["plastisol"])+(harga["warna"]*(jwdes)))*ukxxxl)
        except ValueError:
            print("\nXXXXXXXXXXXXXXXX Input salah format XXXXXXXXXXXXXXXX")
            print()
            continue

        if jumka == uks+ukm+ukl+ukxl+ukxxl+ukxxxl:
            if jwdes >= 0:
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