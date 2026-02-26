import data_input
import function

continueConfirmation = 1

nomorTes = 0

print("""
Selenium Login test HowLongToBeat

Masukkan nomor sesuai salah satu tes uji dibawah!

1: test login dengan kredinsial valid

2: test login dengan kredinsial belum terdaftar
      
3: test login dengan kredinsial password salah

4: test login dengan kredinsial username kosong

5: test login dengan kredinsial password kosong

6: test login dengan kredinsial username karakter khusus(@,#,$, dll)

7: test login dengan kredinsial username kurang karakter

8: test login dengan kredinsial username lebih karakter

9: test login dengan kredinsial username mengandung spasi

10: test login dengan kredinsial password kurang karakter

11: test login dengan kredinsial password lebih karakter

12: test login dengan kredinsial password kurang kapital

13: test login dengan kredinsial password kurang nomor
      
      
note: silahkan ubah input pada file input.py untuk mengubah data input
      
""")

while continueConfirmation == 1:
    while nomorTes < 1 or nomorTes > 13:
        print("Nomor tes uji: ")

        nomorTes = int(input())    

        if nomorTes < 1 or nomorTes > 13:
            print("Silahkan masukkan nomor pada salah satu tes uji tersebut")

    match nomorTes:
        case 1:
            function.melakukanLogin(**data_input.validKredensial)
        
        case 2:
            function.melakukanLogin(**data_input.kredensialBelumTerdaftar)
        
        case 3:
            function.melakukanLogin(**data_input.kredensialPasswordSalah)

        case 4:
            function.melakukanLogin(**data_input.kredensialUsernameKosong)

        case 5:
            function.melakukanLogin(**data_input.kredensialPasswordKosong)

        case 6:
            function.melakukanLogin(**data_input.kredensialUsernameKarakterKhusus)

        case 7:
            function.melakukanLogin(**data_input.kredensialUsernameKurangKarakter)

        case 8:
            function.melakukanLogin(**data_input.kredensialUsernameLebihKarakter)

        case 9:
            function.melakukanLogin(**data_input.kredensialUsernameMengandungSpasi)

        case 10:
            function.melakukanLogin(**data_input.kredensialPasswordKurangKarakter)

        case 11:
            function.melakukanLogin(**data_input.kredensialPasswordLebihKarakter)

        case 12:
            function.melakukanLogin(**data_input.kredensialPasswordKurangKapital)
        
        case 13:
            function.melakukanLogin(**data_input.kredensialPasswordKurangNomor)

    nomorTes = 0

    print("Apakah anda ingin melanjutkan tes? 1: Iya 0: Tidak")
    continueConfirmation = int(input())

    while continueConfirmation < 0 or continueConfirmation > 1:
        print("Silahkan masukkan 1 atau 0")
        continueConfirmation = int(input())
            
        


    

