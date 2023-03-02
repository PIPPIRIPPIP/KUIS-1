'''
Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi KUIS 1 dalam mata kuliah Desain Pemrograman Berorientasi Objek
untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

from kios import Kios
from kios import PemilikKios
from kios import PembagianTransaksiPerHari
from transaksi import Transaksi
from transaksi import Makanan
from transaksi import Minuman
from karyawan import KaryawanKios
from karyawan import KaryawanPengelola

dataKios = []
dataPemilik = []
dataMakanan = []
dataMinuman = []
dataKaryawanKios = []
dataKaryawanPengelola = []
dataTransaksi = []

# DATA KIOS
kios1 = Kios("K01", "Monggo Moro", "Joko")
dataKios.append(kios1)
kios2 = Kios("K02", "Sedap Malam", "Joko")
dataKios.append(kios2)
kios3 = Kios("K03", "Janji Jawa", "Slamet")
dataKios.append(kios3)

# DATA PEMILIK KIOS
pemilik1 = PemilikKios(kios1, "PK01", "360411", "Joko", "Bandung")
pemilik1.addKios(kios2)
dataPemilik.append(pemilik1)
pemilik2 = PemilikKios(kios3, "PK02", "360412", "Slamet", "Bandung Timur")
dataPemilik.append(pemilik2)

# DATA KARYAWAN
karyawan1 = KaryawanKios("K01", "360413", "Rahmat", "Bandung", "Jumat")
dataKaryawanKios.append(karyawan1)
karyawan2 = KaryawanKios("K02", "360414", "Salma", "Cimahi", "Sabtu")
dataKaryawanKios.append(karyawan2)
karyawan3 = KaryawanPengelola("K03", "360415", "Nayl", "Bandung", "Kamis")
dataKaryawanPengelola.append(karyawan3)
karyawan4 = KaryawanPengelola("K04", "360416", "Octo", "Cibiru", "Senin")
dataKaryawanPengelola.append(karyawan4)

# DATA MAKANAN
makanan1 = Makanan(10000, "A01", "K01", "Burger", "Makanan cepat saji")
dataMakanan.append(makanan1)
makanan2 = Makanan(3000, "A02", "K01", "Lemper", "Makanan tradisional")
dataMakanan.append(makanan2)
makanan3 = Makanan(5000, "A03", "K02", "Mendoan", "Gorengan")
dataMakanan.append(makanan3)

# DATA MINUMAN
minuman1 = Minuman(7000, "B01", "K02", "Es Teh", "Minuman Menyegarkan")
dataMinuman.append(minuman1)
minuman2 = Minuman(10000, "B02", "K01", "Matcha Latte", "Minuman kekinian")
dataMinuman.append(minuman2)
minuman3 = Minuman(9000, "B03", "K01", "Cappucino", "Minuman kekinian")
dataMinuman.append(minuman3)

# DATA TRANSAKSI
penjualan1 = Transaksi(makanan2, minuman2, karyawan3, karyawan1, "K01", "1 Maret 2022")
penjualan1.addMakanan(makanan1)
penjualan1.addMakanan(makanan1)

print("       DATABASE DESA       ")
print("===========================")
print("Data kios yang tersedia:")
for i in range(len(dataKios)):
    print(str(i+1) + f".Kode Kios    : {dataKios[i].getKode()}")
    print(          f"  Nama kios    : {dataKios[i].getNamaKios()}")
    print(          f"  Pemilik kios : {dataKios[i].getPemilik()}")

print("---------------------------")
print("Data pemilik setiap kios:")
for i in range(len(dataPemilik)):
    print(str(i+1) + f".Kode Pemilik Kios : {dataPemilik[i].getKodePemilik()}")
    print(          f"  No KTP            : {dataPemilik[i].getKTP()}")
    print(          f"  Nama              : {dataPemilik[i].getNama()}")
    print(          f"  Alamat            : {dataPemilik[i].getAlamat()}")

print("---------------------------")
print("Data makanan yang dijual:")
for i in range(len(dataMakanan)):
    print(str(i+1) + f".Kode Makanan : {dataMakanan[i].getKodeMakanan()}")
    print(          f"  Kode Kios    : {dataMakanan[i].getKodeKios()}")
    print(          f"  Nama Makanan : {dataMakanan[i].getNamaMakanan()}")
    print(          f"  Harga        : Rp. {dataMakanan[i].getHarga()},-")
    print(          f"  Keterangan   : {dataMakanan[i].getKeterangan()}")

print("---------------------------")
print("Data minuman yang dijual:")
for i in range(len(dataMinuman)):
    print(str(i+1) + f".Kode Minuman : {dataMinuman[i].getKodeMinuman()}")
    print(          f"  Kode Kios    : {dataMinuman[i].getKodeKios()}")
    print(          f"  Nama Minuman : {dataMinuman[i].getNamaMinuman()}")
    print(          f"  Harga        : Rp. {dataMinuman[i].getHarga()},-")
    print(          f"  Keterangan   : {dataMinuman[i].getKeterangan()}")

print("---------------------------")
print("Data karyawan:")
for i in range(len(dataKaryawanKios)):
    print(str(i+1) + f".Kode Karyawan : {dataKaryawanKios[i].getKodeKaryawan()}")
    print(          f"  No KTP        : {dataKaryawanKios[i].getKTP()}")
    print(          f"  Nama          : {dataKaryawanKios[i].getNama()}")
    print(          f"  Alamat        : {dataKaryawanKios[i].getAlamat()},-")
    print(          f"  Hari Libur    : {dataKaryawanKios[i].getLibur()}")
for i in range(len(dataKaryawanPengelola)):
    print(str(i+1) + f".Kode Karyawan : {dataKaryawanPengelola[i].getKodeKaryawan()}")
    print(          f"  No KTP        : {dataKaryawanPengelola[i].getKTP()}")
    print(          f"  Nama          : {dataKaryawanPengelola[i].getNama()}")
    print(          f"  Alamat        : {dataKaryawanPengelola[i].getAlamat()},-")
    print(          f"  Hari Libur    : {dataKaryawanPengelola[i].getLibur()}")

print("\n       TRANSAKSI           ")
print("===========================")
penjualan1.cetakTransaksi()