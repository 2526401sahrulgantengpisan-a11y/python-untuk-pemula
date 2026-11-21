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