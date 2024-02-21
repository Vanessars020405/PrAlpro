gaji_per_jam = int(input("masukkan gaji yang diinginkan Rp "))
jmlh_jam_kerja = int(input("masukkan jam kerja per minggu: "))*5 

pdptn_sblm_pajak = gaji_per_jam * jmlh_jam_kerja
print(f"pendapatan_sebelum_pajak: Rp {pdptn_sblm_pajak}")

pdptn_stlh_pajak = pdptn_sblm_pajak - (pdptn_sblm_pajak * 14 /100)
print(f"pedptn_stlh_pajak: Rp {pdptn_stlh_pajak}")

pakaian_aksesoris = pdptn_stlh_pajak * 10/100
print(f"biaya yang digunakan untuk membeli pakaian dan aksesoris: Rp {pakaian_aksesoris}")

alattulis = pdptn_stlh_pajak * 1/100
print(f"biaya yang digunakan untuk membeli alat tulis: Rp {alattulis}")

sedekah = (pdptn_stlh_pajak- (pakaian_aksesoris + alattulis)) * (25/100)
print(f"jumlah uang yang digunakan budi untuk sedekah: Rp {sedekah}")

yatim = 0
dhuafa = 0

sedekah2 = (pdptn_stlh_pajak - (pakaian_aksesoris + alattulis)) * (25/100)
while sedekah2 > 1000:
    sedekah2 -= 1000    
    yatim += (1000 * (30/100))
    dhuafa += (1000 * (70/100))

print(f"jumlah uang yang diberikan budi untuk kaum yatim: Rp {yatim}")
print(f"jumlah uang yang diberikan budi untuk kaum dhuafa: Rp {dhuafa}")
