def menghitung_nilai_tukar_duit(jumlah_rupiah, mata_uang_tujuan):
    nilai_mata_uang = {
        "US Dollar": 0.65,
        "YEN Jepang": 96.56,
        "Ringgit Malaysia": 3.05
    }
    if mata_uang_tujuan not in nilai_mata_uang:
        raise ValueError(
            "Jangan Typo Bossque wkwk : " + ", ".join(nilai_mata_uang)
        )
    else:
        nilai_tukar = nilai_mata_uang[mata_uang_tujuan]
        jumlah_mata_uang_tujuan = jumlah_rupiah / nilai_tukar
        return jumlah_mata_uang_tujuan

try:
    jumlah_rupiah = float(input("Masukkan jumlah rupiah yang ingin dikonversikan : "))
    mata_uang_tujuan = input('Masukkan mata uang yang dituju: ')
    jumlah_mata_uang_tujuan = menghitung_nilai_tukar_duit(jumlah_rupiah, mata_uang_tujuan)
    print('CMIIW')
    print('Nilai {} Rupiah ke {} adalah: {} {}'.format(
        jumlah_rupiah, mata_uang_tujuan, jumlah_mata_uang_tujuan, mata_uang_tujuan))
except ValueError:
    print("===========================")
    print("[Salah input, Ngulang lagi]")
    print("===========================")
except KeyboardInterrupt:
    print("[Salah input, Ngulang lagi]")

except EOFError:
    print("===========================")
    print("[Salah input, Ngulang lagi]")
    print("===========================")

