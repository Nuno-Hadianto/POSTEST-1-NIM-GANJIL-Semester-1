INI ADALAH KODE KONVERSI DUIT

```
    nama = input ("Masukkan Nama : ")
    nim  = input("Masukkan Nim :")
    tempat_tanggal_lahir = input("Masukkan Tempat, Tanggal, Lahir :")
    Asal_Daerah = input("Asal Daerah :")
    Asal_Sekolah = input("Asal Sekolah :")
    motto_hidup = input("Motto Hidup :")

    print(nama)
    print(nim)
    print(tempat_tanggal_lahir)
    print(Asal_Daerah)
    print(Asal_Sekolah)
    print(motto_hidup)

    def menghitung_nilai_tukar_duit(jumlah_rupiah,mata_uang_tujuan):
        nilai_mata_uang = {
            "US Dollar": 0.65,
            "YEN Jepang": 96.56,
            "Ringgit Malaysia": 3.05,
    }

    if mata_uang_tujuan not in nilai_mata_uang:
        raise ValueError(
            "Jangan Typo Bossque wkwk : " + ", ".join(nilai_mata_uang)
        )

    nilai_tukar = nilai_mata_uang[mata_uang_tujuan]
    jumlah_mata_uang_tujuan = jumlah_rupiah / nilai_tukar
    return jumlah_mata_uang_tujuan

    if __name__ :
    #__name__ adalah variabel bawaan yang mengevaluasi nama modul atau skrip saat ini.
    jumlah_rupiah = float(input("Masukkan jumlah rupiah yang ingin dikonversikan : "))
    mata_uang_tujuan = input("Masukkan mata uang yang dituju: ")
    jumlah_mata_uang_tujuan = menghitung_nilai_tukar_duit(jumlah_rupiah, mata_uang_tujuan)
    print("CMIIW")
    print("Nilai {} Rupiah ke {} adalah: {} {}".format(jumlah_rupiah, mata_uang_tujuan, jumlah_mata_uang_tujuan, mata_uang_tujuan))

```
![1](https://github.com/Nuno-Hadianto/POSTEST-1-NIM-GANJIL/assets/63713816/d320e440-9670-4834-921d-7e1585501be1)
![2](https://github.com/Nuno-Hadianto/POSTEST-1-NIM-GANJIL/assets/63713816/dffdb1be-d940-4142-ac67-fa67e8f1adce)
![3](https://github.com/Nuno-Hadianto/POSTEST-1-NIM-GANJIL/assets/63713816/59c8f067-bb7c-4640-acf0-616d9b997680)
![4](https://github.com/Nuno-Hadianto/POSTEST-1-NIM-GANJIL/assets/63713816/f4fd0b74-b048-4268-9718-11d6599147ed)

** PENJELASAN KODE **

fungsi menghitung_nilai_tukar_duit() menerima dua argumen: jumlah_rupiah yang ingin dikonversi dan mata_uang_tujuan. lalu memeriksa apakah mata uang tujuan didukung. Jika tidak, fungsi ini akan mencetak pesan error. Jika mata uang tujuan didukung, fungsi ini akan menghitung nilai_tukar berdasarkan kode mata uang yang didukung oleh kodingan di atas. fungsi ini kemudian akan menghitung jumlah_mata_uang_tujuan yang setara dengan jumlah_rupiah yang diberikan. fungsi ini akan mengembalikan jumlah_mata_uang_tujuan dalam bentuk float dikarenakan jumlah_rupiah. fungsi _name_ meminta input dari pengguna untuk jumlah_rupiah dan mata_uang_tujuan. habistu fungsi ini kemudian akan memanggil fungsi menghitung_nilai_tukar_duit() untuk menghitung nilai tukar lewat fungsi jumlah_mata_uang_tujuan. fungsi ini akan mencetak hasil konversi. CMIIW :)

** FLOWCHART **

![Flowchart post tes 1 drawio](https://github.com/Nuno-Hadianto/POSTEST-1-NIM-GANJIL/assets/63713816/4ae2e158-383a-48b7-b1d4-11042f01e677)

** PENJELASAN OUTPUT **

Flowchart dimulai dengan input dari nama, nim, tempat tanggal lahir, asal daerah, asal sekolah, dan motto hidup. Setelah semua data dimasukkan, program mencetak semua data tersebut. Selanjutnya, program meminta input jumlah rupiah yang ingin dikonversikan ke mata uang tujuan. kemudian memeriksa apakah mata uang tujuan valid atau tidak valid. Jika tidak valid, akan menimbulkan ValueError(error karena typo). Jika mata uang tujuan valid, program menghitung nilai tukar dan mencetak hasil konversinya. flowchart berakhir setelah mencetak hasil konversi.
