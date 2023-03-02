'''
Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi KUIS 1 dalam mata kuliah Desain Pemrograman Berorientasi Objek
untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

class Makanan:
    __kodeMakanan = ""
    __kodeKios = ""
    __namaMakanan = ""
    __harga = 0
    __keterangan = ""

    def __init__(self, harga, kode="", kios="", nama="", keterangan=""):
        self.__kodeMakanan = kode
        self.__kodeKios = kios
        self.__namaMakanan = nama
        self.__harga = harga
        self.__keterangan = keterangan

    # Setter
    def setKodeMakanan(self, kode=""):
        self.__kodeMakanan = kode

    def setKodeKios(self, kode=""):
        self.__kodeKios = kode

    def setNamaMakanan(self, nama=""):
        self.__namaMakanan = nama

    def setHarga(self, harga):
        self.__harga = harga

    def setKeterangan(self, ket=""):
        self.__keterangan = ket
    
    # Getter
    def getKodeMakanan(self):
        return self.__kodeMakanan
    
    def getKodeKios(self):
        return self.__kodeKios
    
    def getNamaMakanan(self):
        return self.__namaMakanan
    
    def getHarga(self):
        return self.__harga
    
    def getKeterangan(self):
        return self.__keterangan
    

class Minuman:
    __kodeMinuman = ""
    __kodeKios = ""
    __namaMinuman = ""
    __harga = 0
    __keterangan = ""

    def __init__(self, harga, kode="", kios="", nama="", keterangan=""):
        self.__kodeMinuman = kode
        self.__kodeKios = kios
        self.__namaMinuman = nama
        self.__harga = harga
        self.__keterangan = keterangan

    # Setter
    def setKodeMinuman(self, kode=""):
        self.__kodeMinuman = kode

    def setKodeKios(self, kode=""):
        self.__kodeKios = kode

    def setNamaMinuman(self, nama=""):
        self.__namaMinuman = nama

    def setHarga(self, harga):
        self.__harga = harga

    def setKeterangan(self, ket=""):
        self.__keterangan = ket
    
    # Getter
    def getKodeMinuman(self):
        return self.__kodeMinuman
    
    def getKodeKios(self):
        return self.__kodeKios
    
    def getNamaMinuman(self):
        return self.__namaMinuman
    
    def getHarga(self):
        return self.__harga
    
    def getKeterangan(self):
        return self.__keterangan
    
class Transaksi:
    __kodeKios = ""
    __tanggal = ""
    __kodeMakanan = []
    __kodeMinuman = []

    def __init__(self, makanan, minuman, karyawanPengelola, karyawanKios="", kode="", tanggal=""):
        self.__kodeKios = kode
        self.__tanggal = tanggal
        self.__kodeMakanan.append(makanan)
        self.__kodeMinuman.append(minuman)
        self.__kodeKaryawanKios = karyawanKios
        self.__kodeKaryawanPengelola = karyawanPengelola

    # Setter
    def setKodeKios(self, kode):
        self.__kodeKios = kode

    def setTanggal(self, tanggal):
        self.__tanggal = tanggal

    def addMakanan(self, makanan):
        self.__kodeMakanan.append(makanan)

    def addMinuman(self, minuman):
        self.__kodeMinuman.append(minuman)

    def setKaryawan(self, karyawanKios):
        self.__kodeKaryawanKios = karyawanKios

    def setKodeKaryawanPengelola(self, karyawanPengelola):
        self.__kodeKaryawanPengelola = karyawanPengelola

    # Getter
    def getKodeKios(self):
        return self.__kodeKios

    def getTanggal(self):
        return self.__tanggal 

    def getKodeMakanan(self):
        return self.__kodeMakanan 

    def getKodeMinuman(self):
        return self.__kodeMinuman 

    def getKodeKaryawanKios(self):
        return self.__kodeKaryawanKios 
        
    def getKodeKaryawanPengelola(self):
        return self.__kodeKaryawanPengelola 
    
    def getTotal(self):
        total = 0
        for i in range(len(self.__kodeMakanan)):
            total += self.__kodeMakanan[i].getHarga()
        for i in range(len(self.__kodeMinuman)):
            total += self.__kodeMinuman[i].getHarga()

        return total
    
    def cetakTransaksi(self):
        print(f"Tanggal Transaksi     : {self.__tanggal}")
        print(f"Kode Kios             : {self.__kodeKios}")
        print(f"Karyawan Yang bertugas: {self.__kodeKaryawanKios.getNama()}")
        print(f"Karyawan Pengelola    : {self.__kodeKaryawanPengelola.getNama()}")
        print(f"Makanan Terjual : ")
        for i in range(len(self.__kodeMakanan)):
            print(f"- {self.__kodeMakanan[i].getNamaMakanan()}")
        print(f"Minuman Terjual : ")
        for i in range(len(self.__kodeMinuman)):
            print(f"- {self.__kodeMinuman[i].getNamaMinuman()}")
        print(f"Total Harga: Rp. {self.getTotal()},-")
