'''
Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi KUIS 1 dalam mata kuliah Desain Pemrograman Berorientasi Objek
untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

class Kios:
    __kodeKios = ""
    __namaKios = ""
    __namaPemilik = ""

    def __init__(self, kode="", nama="", pemilik=""):
        self.__kodeKios = kode
        self.__namaKios = nama
        self.__namaPemilik = pemilik

    # Setter
    def setKode(self, kode):
        self.__kodeKios = kode

    def setNamaKios(self, nama):
        self.__namaKios = nama

    def setPemilik(self, pemilik):
        self.__namaPemilik = pemilik

    # Getter
    def getKode(self):
        return self.__kodeKios 

    def getNamaKios(self):
        return self.__namaKios 

    def getPemilik(self):
        return self.__namaPemilik 
    
class PemilikKios:
    __kodePemilikKios = ""
    __kodeKios = []
    __NoKTP = ""
    __nama= ""
    __alamat= ""

    def __init__(self, kios, kode="", ktp="", nama="", alamat=""):
        self.__kodePemilikKios = kode
        self.__kodeKios.append(kios)
        self.__NoKTP = ktp
        self.__nama = nama
        self.__alamat = alamat

    # Setter
    def setKodePemilik(self, kode):
        self.__kodePemilikKios = kode

    def addKios(self, kios):
        self.__kodeKios.append(kios)

    def setKTP(self, ktp):
        self.__NoKTP = ktp

    def setNama(self, nama):
        self.__nama = nama

    def setAlamat(self, alamat):
        self.__alamat = alamat

    # Getter
    def getKodePemilik(self):
        return self.__kodePemilikKios 
    
    def getKodeKios(self):
        return self.__kodeKios

    def getKTP(self):
        return self.__NoKTP 

    def getNama(self):
        return self.__nama 

    def getAlamat(self):
        return self.__alamat
    

class PembagianTransaksiPerHari:
    __kodeKios = ""
    __omsetDibagikan = ""
    __bagianPengelola = ""
    __tanggal = ""

    def __init__(self, kode="", omset="", pengelola="", tanggal=""):
        self.__kodeKios = kode
        self.__omsetDibagikan = omset
        self.__bagianPengelola = pengelola
        self.__tanggal = tanggal

    # Setter
    def setKode(self, kode):
        self.__kodeKios = kode
    
    def setOmset(self, omset):
        self.__omsetDibagikan = omset
    
    def setPengelola(self, pengelola):
        self.__bagianPengelola = pengelola
    
    def setTanggal(self, tanggal):
        self.__tanggal = tanggal

    # Getter
    def getKode(self):
        return self.__kodeKios 
    
    def getOmset(self):
        return self.__omsetDibagikan 
    
    def getPengelola(self):
        return self.__bagianPengelola 
    
    def getTanggal(self):
        return self.__tanggal 