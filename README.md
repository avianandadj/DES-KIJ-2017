# DES-KIJ-2017
DES algorithm with CBC method for KIJ class

Data Encryption Standard (DES) termasuk ke dalam sistem kriptografi simetri dan tergolong jenis cipher blok. DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit plainteks menjadi 64 bit cipherteks dengan menggunakan 56 bit kunci internal (internal key) atau upa-kunci (subkey). Kunci internal dibangkitkan dari kunci eksternal (external key) yang panjangnya 64 bit.

DES dengan metode CBC:
1. Untuk fase pertama, kita menggunakan Initialization Vector (IV) sebagai nilai awal untuk di XOR kan dengan plaintext.
2. Selanjutnya, blok plaintext tersebut dilakukan enkripsi dengan key 56 bit yang kemudian
3. akan menghasilkan blok ciphertext
4. Blok ciphertext tersebut akan di XOR kan lagi dengan blok plaintext selanjutnya.

