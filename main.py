import input
import function

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

nomorTes = input("Nomor tes uji:")

match nomorTes:
    case 1:
        function.melakukanLogin(**input.validKredensial)
    
    case 2:
        function.melakukanLogin(**input.kredensialBelumTerdaftar)
    
    case 3:
        function.melakukanLogin(**input.kredensialPasswordSalah)

    case 4:
        function.melakukanLogin(**input.kredensialUsernameKosong)

    case 5:
        function.melakukanLogin(**input.kredensialPasswordKosong)

    case 6:
        function.melakukanLogin(**input.kredensialUsernameKarakterKhusus)

    case 7:
        function.melakukanLogin(**input.kredensialUsernameKurangKarakter)

    case 8:
        function.melakukanLogin(**input.kredensialUsernameLebihKarakter)

    case 9:
        function.melakukanLogin(**input.kredensialUsernameMengandungSpasi)

    case 10:
        function.melakukanLogin(**input.kredensialPasswordKurangKarakter)

    case 11:
        function.melakukanLogin(**input.kredensialPasswordLebihKarakter)

    case 12:
        function.melakukanLogin(**input.kredensialPasswordKurangKapital)
    
    case 13:
        function.melakukanLogin(**input.kredensialPasswordKurangNomor)
