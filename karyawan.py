'''
Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi KUIS 1 dalam mata kuliah Desain Pemrograman Berorientasi Objek
untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

class KaryawanKios:
    __kodeKaryawanKios = ""
    __NoKTP = ""
    __nama = ""
    __alamat = ""
    __liburShift = ""

    def __init__(self, kode="", ktp="", nama="", alamat="", libur=""):
        self.__kodeKaryawanKios = kode
        self.__NoKTP = ktp
        self.__nama = nama
        self.__alamat = alamat
        self.__liburShift = libur

    # Setter
    def setKodeKaryawan(self, kode):
        self.__kodeKaryawanKios = kode

    def setKTP(self, ktp):
        self.__NoKTP = ktp

    def setNama(self, nama):
        self.__nama = nama

    def setAlamat(self, alamat):
        self.__alamat = alamat

    def setLibur(self, libur):
        self.__liburShift = libur

    # Getter
    def getKodeKaryawan(self):
        return self.__kodeKaryawanKios 

    def getKTP(self):
        return self.__NoKTP 

    def getNama(self):
        return self.__nama 

    def getAlamat(self):
        return self.__alamat 

    def getLibur(self):
        return self.__liburShift 

class KaryawanPengelola:
    __kodeKaryawanPengelola = ""
    __NoKTP = ""
    __nama = ""
    __alamat = ""
    __liburShift = ""

    def __init__(self, kode="", ktp="", nama="", alamat="", libur=""):
        self.__kodeKaryawanPengelola = kode
        self.__NoKTP = ktp
        self.__nama = nama
        self.__alamat = alamat
        self.__liburShift = libur

    # Setter
    def setKodeKaryawan(self, kode):
        self.__kodeKaryawanPengelola = kode

    def setKTP(self, ktp):
        self.__NoKTP = ktp

    def setNama(self, nama):
        self.__nama = nama

    def setAlamat(self, alamat):
        self.__alamat = alamat

    def setLibur(self, libur):
        self.__liburShift = libur

    # Getter
    def getKodeKaryawan(self):
        return self.__kodeKaryawanPengelola 

    def getKTP(self):
        return self.__NoKTP 

    def getNama(self):
        return self.__nama 

    def getAlamat(self):
        return self.__alamat 

    def getLibur(self):
        return self.__liburShift 