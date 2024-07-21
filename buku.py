print("\n=== NOMOR 1 ===")

class Buku:
    def __init__(self, judul, penulis, konten):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = None
        self.tahun_terbit = None
        self.konten = konten
        self.iktsar = None

    def read(self, halaman_awal, halaman_akhir):
        if halaman_awal < 1 or halaman_akhir > len(self.konten) or halaman_awal > halaman_akhir:
            raise ValueError("Nomor halaman tidak valid.")
        return self.konten[halaman_awal-1:halaman_akhir]

    def __str__(self):
        return f"{self.judul} by {self.penulis}"
