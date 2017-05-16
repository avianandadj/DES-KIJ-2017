# DES-KIJ-2017
DES algorithm with CBC method for KIJ class
Aviananda D.J.  5114100085
Afif Ridho K.P. 5114100173

# Pendahuluan
Data Encryption Standard (DES) termasuk ke dalam sistem kriptografi simetri dan tergolong jenis cipher blok. DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit plainteks menjadi 64 bit cipherteks dengan menggunakan 56 bit kunci internal (internal key) atau upa-kunci (subkey). Kunci internal dibangkitkan dari kunci eksternal (external key) yang panjangnya 64 bit.

# Implementasi
DES dengan metode CBC:
1. Untuk fase pertama, kita menggunakan Initialization Vector (IV) sebagai nilai awal untuk di XOR kan dengan plaintext.
2. Selanjutnya, blok plaintext tersebut dilakukan enkripsi dengan key 56 bit yang kemudian
3. akan menghasilkan blok ciphertext
4. Blok ciphertext tersebut akan di XOR kan lagi dengan blok plaintext selanjutnya.

# Langkah Pada Data Encryption Standard (DES)

    Generate Subkeys
    1.1 Memasukkan key yang ingin digunakan. Key ini akan sama dengan key yang akan digunakan untuk proses decryption. Key juga jumlahnya harus tepat 64 bitd
    1.2 Key akan dipermutasi dengan menjadi 56 bit
    1.3 Key akan dibagi dua menjadi C0 (28 bit pertama) dan D0 (28 bit terakhir)
    1.4 Setiap C0 dan Do di shift ke kiri menjadi C1 dan D1. C1D1 akan menjadi subkey ke-1 atau K1
    1.5 Lakukan langkah 1.4 hingga didapatkan K16

    Generate Chiper Text
    2.1 Message yang ingin dienkripsi kan dilakukan permutasi awal (Initiate Permutation) 2.2 Setalah itu, binary yang didapatkan akan dibagi dua menjadi L0 (32 bit pertama) dan R0 (32 bit terakhir)
    2.3 Lalu dilakukan iterasi 16 kali dengan ketentuan L1 = R0 dan R1 = L0 = f(Ro, K1) (Rincian rumus ini akan
    dilampirkan kemudian)
    2.4 Hasil iterasi ke-16 adalah L16 dan R16 yang kemudian digabungkan
    2.5 L16+R16 adalah hasil akhir dari chiper text

Langkah implementasi pada DES dengan algoritma Cipher Block Chaining

Berikut ini merupakan langkah implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Cipher Block Chaining (CBC):

    Enkripsi
    1.1 CBC menggunakan plaintext sebagai input pada algoritma DES
    1.2 Plaintext nantinya akan di XOR dengan IV
    1.3 Output dari XOR antara plaintext dan IV akan dienkripsi dengan key yang sudah diberikan
    1.4 Hasil akhir yang keluar akan digunakan sebagai IV untuk putaran selanjutnya
    
    Dekripsi
    1.1 Dekripsi pada CBC menggunakan algoritma yang hampir sama dengan enkripsi CBC
    1.2 Bedanya adalah urutan subkey dibalik dari key paling akhir (ke-16) menjadi key pertama (ke-1)

Encrypted Chat
    
    1.1 Chat menggunakan metode socket dengan modul select agar dapat menangani banyak client
    1.2 Pesan di enkripsi secara end-to-end (dienkripsi pada client dan didekripsi pada client)
    1.3 Pada program chat ini kami menggunakan library subprocess pada python untuk menjalankan file des.py (enkripsi) dan file decrypt-des.py (dekripsi)

Diffie-hellman

        def run():
            q=353 # publicly known must be prime
            a=3 # publicly known

            xa=97 # only client1 knows this 
            xb=233 # only client2 knows this

            client1Sends = (a**xa)%q
            client2process = (client1Sends**xb)%q
            client2Sends = (a**xb)%q
            client1process = (client2Sends**xa)%q


            print "client1 sends    ", client1Sends 
            print "client2 process   ", client2process 
            print "client2 sends      ", client2Sends 
            print "client1 process ", client1process

            print "In theory both should have ", (a**(xa*xb))%q

            return client1Sends, client2Computes, client2Sends, client1Computes

    Diffie-hellman adalah metode untuk mendistribusikan key dengan cara client pertama menentukan nilai random x, yang kemudian akan dimasukkan dalam perhitungan yang melihatkan nilai q (bilangan prima) dan a(primitive root)

    rumusnya sharedkeynya adalah: 
    pada client a yang dikirim ke client b: (a^xa) mod q
    pada client b yang dikirim ke client a: (a^xb) mod q

    lalu sharedkey tadi di proses ada masing-masing client 
    pada client a: (((a^xb) mod q)^xa) mod q
    pada client b: (((a^xa) mod q)^xb) mod q

    setelah di proses, kedua client akan mendapatkan key yang sama untuk digunakan pada enkripsi DES.

    
![screenshot_2017-04-28_15-07-06](https://cloud.githubusercontent.com/assets/19360671/25523274/49b5a28c-2c30-11e7-9a2d-c80eb935ee5f.png)

    RSA
        Dalam program ini RSA hanya digunakan untuk sharing private dan public key yang nantinya key tersebut akan digunakan untuk enkripsi dan dekripsi menggunakan algoritma DES.
        Cara mendapatkan key menggunakan algoritma RSA adalah sebagai berikut:
        Langkah 1 :
        Pilih 2 bilangan prima secara acak untuk nilai p & q. Dengan syarat nilai p > q. 
        Sebagai contoh kita akan ambil nilai p = 17  & q = 11

        Langkah 2 :
        Hitung N 
        N = p*q
          = 17 * 11 
          = 187

        Langkah 3 :
        Hitung phi. 
        φ = (p-1)*(q-1)
          = (17-1) * (11-1)
          = 16 * 10
          = 160

        Langkah 4 :
        Pilih nilai e dengan syarat e > 1, dan GCD(e,160) = 1
        sebagai contoh, nilai e yang akan kita ambil adalah 7.

        Kita pastikan apakah GCD(7,160) = 1 ?
        160 mod 7 = 6
        7 mod 6 = 1        

        Ternyata benar GCD(7,160) = 1. Berarti kita dapat menggunakan angka 7 sebagai nilai e.

        Langkah 5 :
        Pilih nilai d, dengan syarat (d.e) mod φ = 1
        sebagai sample, nilai d yang akan kita ambil adalah 283.

        Kita pastikan apakah (283*7) mod 160 = 1 ?
        (283*7) mod 160 
        1981 mod 160 = 61
        160 mod 61 = 38
        61 mod 38 = 23
        38 mod 23 = 15
        23 mod 15 = 8
        8 mod 7 = 1
        
        Ternyata benar (283*7) mod 160 = 1. Berarti persyaratan terpenuhi dan 283 sudah bisa dipastikan dapat mengisi nilai d

        Dengan demikian, kita dapat menyimpulkan bahwa :
        Private key RSA nya adalah :
        n = 187
        d = 283

        Public key RSA nya adalah :
        n = 187
        e = 7

# Referensi:
http://dhost.info/pasjagor/des/start.php?id=0
http://octarapribadi.blogspot.co.id/2012/10/contoh-enkripsi-dengan-algoritma-des.html
http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
http://github.com/studiawan
https://gist.github.com/JonCooperWorks/5314103
http://teknosian.blogspot.co.id/2014/06/5-langkah-mudah-membuat-kunci-algoritma.html
