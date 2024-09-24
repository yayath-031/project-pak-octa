# Dataset permainan
permainan = [
    {
        "Judul": "Mobile Legends: Bang Bang",
        "Developer": ["Moonton"],
        "Tahun terbit": "2016",
        "Genre": ["MOBA", "Action", "Strategy", "Fight"]
    },
    {
        "Judul": "Garena Free Fire",
        "Developer": ["Garena"],
        "Tahun terbit": "2018",
        "Genre": ["Battle Royale", "Action"]
    },
    {
        "Judul": "PUBG Mobile",
        "Developer": ["Tencent Games"],
        "Tahun terbit": "2018",
        "Genre": ["Battle Royale", "Shooter"]
    },
    {
        "Judul": "Call of Duty: Mobile",
        "Developer": ["TiMi Studios (Tencent)"],
        "Tahun terbit": "2019",
        "Genre": ["First-Person Shooter"]
    }
]

# Fungsi untuk menarik data berdasarkan kriteria
def tarik_data_berdasarkan_kriteria(kriteria, nilai):
    hasil = []
    
    for item in permainan:
        if nilai.lower() in [x.lower() for x in item.get(kriteria, [])]:  # Mencari dalam list kriteria
            # Format output
            format_output = f'"{item["Judul"]} ({", ".join(item["Genre"])}) ({item["Tahun terbit"]})"'
            hasil.append(format_output)
    
    if hasil:
        return "\n".join(hasil)
    else:
        return f'Tidak ada permainan yang ditemukan dengan {kriteria} "{nilai}".'

# Mengambil input dari pengguna
kriteria = input("Masukkan kriteria (Developer, Tahun terbit, Genre): ").capitalize()  # Mengambil input kriteria
nilai = input(f"Masukkan nilai yang ingin dicari untuk {kriteria}: ")  # Mengambil input nilai yang ingin dicari

# Menampilkan hasil
data_permainan = tarik_data_berdasarkan_kriteria(kriteria, nilai)
print(data_permainan)
