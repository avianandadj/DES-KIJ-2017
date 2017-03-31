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
    1.1 Memasukkan key yang ingin digunakan. Key ini akan sama dengan key yang akan digunakan untuk proses decryption. Key juga jumlahnya harus tepat 64 bit
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
    

# Referensi:
http://dhost.info/pasjagor/des/start.php?id=0
http://octarapribadi.blogspot.co.id/2012/10/contoh-enkripsi-dengan-algoritma-des.html
http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
