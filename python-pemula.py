print("Halo Python")

# Tipe data floating numbers
a = 7.5

print(a)


# Tipe data integers
x = 5
y = 3
z = 5 + 3

print(z)











# ===== 2. String =====

# Menggunakan single quote
myFirstName = 'Rizqi'

# Menggunakan double quote
myLastName = "Maulana"

# Penulisan angka sebagai string
myAge = "25"

# Penulisan string multiline
myHobby = """Hobi saya adalah
bersepeda dan bermain game.
"""

# Mencetak variabel string dengan perintah print
print(myFirstName + " " + myLastName)
print("Umur saya " + myAge)
print(myHobby)















# ===== 3. Boolean =====

# Contoh penulisan boolean yang benar
a = True
b = False

print(a)
print(b)

# Contoh penulisan boolean yang salah
# Jika dijalankan, pada baris ini akan error
# c = true

# print(c)















# ===== 4. Operator Aritmatika =====

a = 4
b = 2
# Penjumlahan
c = a + b
# Pengurangan
d = a - b
# Perkalian
e = a * b
# Pembagian
f = a / b
# Modulus
g = a % b
# Eksponensial
h = a ** b

# Cetak output
print(c)  # 6
print(d)  # 2
print(e)  # 8
print(f)  # 2.0
print(g)  # 0
print(h)  # 16










# ===== 5. Operator Perbandingan =====

a = 3
b = 5
# Perbandingan sama dengan
c = a == b
# Perbandingan tidak sama dengan
d = a != b
# Perbandingan lebih kecil
e = a < b
# Perbandingan lebih kecil sama dengan
f = a <= b
# Perbandingan lebih besar
g = a > b
# Perbandingan lebih besar sama dengan
h = a >= b

# Cetak output
print(c)  # False
print(d)  # True
print(e)  # True
print(f)  # True
print(g)  # False
print(h)  # False








# ===== 6. Operator Logika =====

a = 3
b = 9

# Contoh penggunaan "and"
print(a < 5 and b > 6)  # True
print(a < 5 and b < 6)  # False
print(a > 5 and b < 6)  # False

# Contoh penggunaan "or"
print(a < 5 or b > 6)  # True
print(a < 5 or b < 6)  # True
print(a > 5 or b < 6)  # False

# Contoh penggunaan "not"
print(not(a < 5 or b > 6))  # False
print(not(a > 5 or b < 6))  # True









# ===== 7. Percabangan (if, elif, else) =====

"""
Note:
Penulisan kode di dalam blok atau scope pada Python bergantung pada
Indentation (spasi di awal baris). Contoh jika kita ingin menulis kode
di dalam blok/scope statemen if, maka penulisannya seperti ini:
"""

# Penulisan yang benar:
if(True):
    print("Benar.")  # ada spasi di awal baris (lebih menjorok ke dalam)

# Penulisan yang salah:
# if(True):
# print("Benar.")  # tidak ada spasi di awal baris

x = 5
y = 10

# Karena x lebih kecil dari y adalah benar, kode di dalam if dijalankan.
if(x < y):
    print("nilai x lebih kecil dari y.")  # ini akan dijalankan

# Karena x lebih besar dari y adalah salah, kode di dalam if tidak dijalankan.
if(x > y):
    print("nilai x lebih besar dari y.")  # ini tidak akan dijalankan

a = 80

# Pengecekan pertama dengan if: if(a > 90)
# Pengecekan kedua dengan elif: elif(a > 70)
if(a > 90):
    print("Dapat nilai A.")  # ini tidak akan dijalankan
elif(a > 70):
    print("Dapat nilai B.")  # ini akan dijalankan

a = 60

if(a > 90):
    print("Dapat nilai A.")  # ini tidak akan dijalankan
elif(a > 70):
    print("Dapat nilai B.")  # ini tidak akan dijalankan
else:
    print("Dapat nilai C.")  # ini akan dijalankan







    

# ===== 8. Perulangan (for, while, break, continue) =====

# Mencetak kata "Halo Python" sebanyak 5 kali
for x in range(5):
    print("Halo Python.")

# Mencetak semua item pada variabel fruits (lists)
fruits = ['Apple', 'Banana', 'Mango', 'Durian']
for fruit in fruits:
    print(fruit)

# Mencetak semua huruf satu per satu pada kata "indonesia"
myCountry = "indonesia"
for x in myCountry:
    print(x)

# Mencetak angka, selama angka lebih kecil dari 5
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Menghentikan perulangan jika nilai x adalah 3
# Walaupun seharusnya perulangan berhenti setelah 5 kali berjalan.
for x in range(5):
    print(x)
    if x == 3:
        break

# Melewati perulangan jika nilai x adalah angka genap (2, 4, 6 dst)
# Hanya angka ganjil yang dicetak karena angka genap di-skip
# menggunakan keyword "continue"
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)