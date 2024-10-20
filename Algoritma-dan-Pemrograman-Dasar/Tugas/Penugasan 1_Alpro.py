# Program Penentuan Kategori Pengeluaran Mingguan Atau Pengeluaran Bulanan Berdasarkan Besarnya Nominal
print(35*"=")
print("   PENGELUARAN PADA RUMAH TANGGA")
print(35*"=" + "\n")

# Input Standar Pengeluaran
standar_pengeluaran_mingguan = 500000
standar_pengeluaran_bulanan = 1500000

# Input Data Pengeluaran Mingguan MInggu Ini
laundry = 26000
air_galon = 6000
transportasi = 35000
makan_dan_minum = 315000
camilan = 50000
minuman_kemasan = 24000


# Input Data Pengeluaran Bulanan Bulan ini
pajak_listrik = 200000
pajak_PDAM = 150000
benlanja_bulanan = 1250000
kuota_internet_bulanan = 120000
simpanan = 500000

# Total Pengeluaran
total_pengeluaran_mingguan = laundry + air_galon + transportasi + makan_dan_minum + camilan + minuman_kemasan
total_pengeluaran_bulanan = pajak_listrik + pajak_PDAM + benlanja_bulanan + kuota_internet_bulanan + simpanan

# Pengategorian Pengeluaran
if total_pengeluaran_mingguan > standar_pengeluaran_mingguan:
    kategori_pengeluaran_mingguan = "Boros"
else:
    kategori_pengeluaran_mingguan = "Hemat"

if total_pengeluaran_bulanan > standar_pengeluaran_bulanan:
    kategori_pengeluaran_bulanan = "Boros"
else:
    kategori_pengeluaran_bulanan = "Hemat"

# Kategori Pengeluaran
print("KATEGORI PENGELUARAN")
print(20*"=" + "\n")
print("Pengeluaran Mingguan Minggu Ini")
print("Laundry: Rp.", laundry)
print("Air galon: Rp.", air_galon)
print("Transportasi: Rp.", transportasi)
print("Makan dan minum: Rp.", makan_dan_minum)
print("Camilan: Rp.", camilan)
print("Minuman kemasan: Rp.", minuman_kemasan)
print(35*"-" + " +")
print("Total pengeluaran: Rp.", total_pengeluaran_mingguan)
print("Kategori pengeluaran: ", kategori_pengeluaran_mingguan)
print("\n")
print("Pengeluaran Mingguan Minggu Ini")
print("Pajak listrik: Rp.", pajak_listrik)
print("Pajak PDAM: Rp.", pajak_PDAM)
print("Belanja bulanan: Rp.", laundry)
print("Kuota internet bulanan: Rp.", kuota_internet_bulanan)
print("Simpanan: Rp.", simpanan)
print(35*"-" + " +")
print("Total pengeluaran: Rp.", total_pengeluaran_bulanan)
print("Kategori pengeluaran: ", kategori_pengeluaran_bulanan)