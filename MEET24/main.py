import fisika
import time

def batas():
    print("-" * 30)

waktu_awal = time.time()

result_massa_jenis = fisika.MassaJenis.massajenis(10, 2)
result_massa = fisika.MassaJenis.massa(10, 2)
result_volume = fisika.MassaJenis.volume(10, 2)

print(f"massa jenis = {result_massa_jenis}")
print(f"massa = {result_massa}")
print(f"volume = {result_volume}")
waktu_akhir = time.time()
print(f"waktu yang dibutuhkan : {waktu_akhir - waktu_awal}")

batas()

print(f"usaha = {fisika.W(10,2)}")
print(f"gaya = {fisika.F(10,2)}")
print(f"jarak = {fisika.M(10,2)}")

batas()

print(f"Hasil Energi Potensial : {fisika.Ep(4, 7, 4)}")

batas()

print(f"Hasil Energi Kinetik : {fisika.Ek(4, 7)}")

batas()

diskon10 = fisika.jl(10)
result = diskon10(10000)
print(f"Diskon 10% = {result}")