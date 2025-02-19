from collections import deque

# Representasi graf MRT sebagai dictionary (stasiun sebagai node, jalur sebagai edge)
graf_krl = {
    "Bogor": ["Cilebut"],
    "Cilebut": ["Bogor", "Bojong Gede"],
    "Bojong Gede": ["Cilebut", "Citayam"],
    "Citayam": ["Bojong Gede", "Pondok Rajeg", "Depok"],
    "Pondok Rajeg": ["Citayam", "Cibinong"],
    "Cibinong": ["Nambo"],
    "Nambo": ["Cibinong"],
    "Depok": ["Citayam", "Depok Baru"],
    "Depok Baru": ["Depok", "Pondok Cina"],
    "Pondok Cina": ["Depok Baru", "Univ.Indonesia"],
    "Univ.Indonesia": ["Pondok Cina", "Univ.Pancasila"],
    "Univ.Pancasila": ["Univ.Indonesia", "Lenteng Agung"],
    "Lenteng Agung": ["Univ.Pancasila", "Tanjung Barat"],
    "Tanjung Barat": ["Lenteng Agung", "Pasar Minggu"],
    "Pasar Minggu": ["Tanjung Barat", "Pasar Minggu Baru"],
    "Pasar Minggu Baru": ["Pasar Minggu", "Duren Kalibata"],
    "Duren Kalibata": ["Pasar Minggu Baru", "Cawang"],
    "Cawang": ["Duren Kalibata", "Tebet"],
    "Tebet": ["Cawang", "Manggarai"],
    "Manggarai": ["Sudirman", "Tebet", "Matraman", "Cikini"],
    "Cikini": ["Manggarai", "Gondangdia"],
    "Gondangdia": ["Cikini", "Juanda"],
    "Juanda": ["Gondangdia", "Sawah Besar"],
    "Sawah Besar": ["Juanda", "Mangga Besar"],
    "Mangga Besar": ["Sawah Besar", "Jayakarta"],
    "Jayakarta": ["Mangga Besar", "Jakarta Kota"],
    "Jakarta Kota": ["Jayakarta", "Kampung Bandan"],
    "Kampung Bandan":["Jakarta Kota", "Angke", "Ancol", "Rajawali"],
    "Angke": ["Kampung Bandan", "Karet"],
    "Karet": ["Angke", "Sudirman"],
    "Sudirman": ["Karet", "Manggarai"],
    "Ancol": ["Kampung Bandan", "Tanjung Priok"],
    "Tanjung Priok": ["Ancol"],
    "Rajawali": ["Kampung Bandan", "Kemayoran"],
    "Kemayoran": ["Rajawali", "Pasar Senen"],
    "Pasar Senen": ["Kemayoran", "Gang Sentiong"],
    "Gang Sentiong": ["Pasar Senen", "Kramat"],
    "Kramat": ["Gang Sentiong", "Pondok Jati"],
    "Pondok Jati": ["Kramat", "Jati Negara"],
    "Jati Negara": ["Pondok Jati", "Matraman", "Klender"],
    "Matraman": ["Jati Negara", "Manggarai"],
    "Klender": ["Jati Negara", "Buaran"],
    "Buaran": ["Klender", "Klender Baru"],
    "Klender Baru": ["Buaran", "Cakung"],
    "Cakung": ["Klender Baru", "Kranji"],
    "Kranji": ["Cakung", "Bekasi"],
    "Bekasi": ["Kranji", "Bekasi Timur"],
    "Bekasi Timur": ["Bekasi", "Tambun"],
    "Tambun": ["Bekasi Timur", "Cibitung"],
    "Cibitung": ["Tambun", "Metland Telaga Murni"],
    "Metland Telaga Murni": ["Cikarang"],
    "Cikarang": ["Metland Telaga Murni"]
}

def rute_terpendek_krl(graf, mulai, selesai):
    antrian = deque([[mulai]])  # Antrian BFS berisi jalur yang ditemukan
    stasiun_yang_telah_dikunjungi = set()  # Set untuk menyimpan stasiun yang sudah dikunjungi

    while antrian:
        jalur = antrian.popleft()  # Ambil jalur pertama dari antrian
        stasiun = jalur[-1]  # Ambil stasiun terakhir dalam jalur saat ini

        if stasiun == selesai:  # Jika sudah sampai tujuan, kembalikan jalurnya
            return jalur
        
        if stasiun not in stasiun_yang_telah_dikunjungi:
            stasiun_yang_telah_dikunjungi.add(stasiun)  # Tandai stasiun sebagai telah dikunjungi
            for tetangga in graf.get(stasiun, []):  # Cek semua stasiun terhubung
                jalur_baru = list(jalur) + [tetangga]  # Buat jalur baru dengan tambahan stasiun
                antrian.append(jalur_baru)  # Tambahkan ke antrian untuk dieksplorasi

    return None  # Jika tidak ada jalur yang ditemukan

# Tambahan kode untuk menampilkan daftar stasiun
print("\nDaftar stasiun yang tersedia:")
print(", ".join(sorted(graf_krl.keys())))  # Menampilkan daftar stasiun dalam urutan alfabetis
print("\nSilakan masukkan stasiun yang tersedia di atas.")

# Tambahan kode untuk input dari pengguna
stasiun_awal = input("Masukkan stasiun awal: ")  # Mengambil input stasiun awal
stasiun_tujuan = input("Masukkan stasiun tujuan: ")  # Mengambil input stasiun tujuan

# Memastikan stasiun yang dimasukkan ada dalam graf
if stasiun_awal in graf_krl and stasiun_tujuan in graf_krl:
    rute_terpendek = rute_terpendek_krl(graf_krl, stasiun_awal, stasiun_tujuan)
    print("Rute Terpendek:", " → ".join(rute_terpendek) if rute_terpendek else "Tidak ditemukan")
else:
    print("Stasiun yang dimasukkan tidak valid. Pastikan stasiun tersebut ada di graf MRT.")  # Menangani input yang tidak valid