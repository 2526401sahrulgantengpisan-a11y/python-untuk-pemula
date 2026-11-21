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









    

# ===== 9. Lists =====

# Membuat lists yang berisi nama-nama hewan
animals = ["Ayam", "Bebek", "Cicak"]

# Mengakses item berdasarkan urutannya (indexing). Indexing dimulai dari 0.
print(animals[1])  # Bebek

# Negative indexing: -1 adalah item terakhir, -2 item kedua dari terakhir
print(animals[-1])  # Cicak
print(animals[-2])  # Bebek

# Menambah item di posisi terakhir dengan "append"
animals = ["Ayam", "Bebek", "Cicak"]
animals.append("Domba")
print(animals)  # ['Ayam', 'Bebek', 'Cicak', 'Domba']

# Menambah item di posisi tertentu dengan "insert"
# Contoh: menambahkan 1 item di posisi ketiga (indexing = 2)
animals.insert(2, "Buaya")
print(animals)  # ['Ayam', 'Bebek', 'Buaya', 'Cicak', 'Domba']

# Menghapus item tertentu dengan "remove"
animals = ["Ayam", "Bebek", "Cicak"]
animals.remove("Bebek")
print(animals)  # ['Ayam', 'Cicak']

# Menghapus item terakhir dengan "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop()
print(animals)  # ['Ayam', 'Bebek']

# Menghapus item berdasarkan posisinya dengan "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop(0)
print(animals)  # ['Bebek', 'Cicak']

# Menghapus semua item dengan "clear"
animals = ["Ayam", "Bebek", "Cicak"]
animals.clear()
print(animals)  # []

# Menggabungkan sebuah lists dengan lists lainnya
animals = ["Ayam", "Bebek", "Cicak"]
otherAnimals = ["Domba", "Elang", "Gajah"]
animals.extend(otherAnimals)
print(animals)  # ['Ayam', 'Bebek', 'Cicak', 'Domba', 'Elang', 'Gajah']

fruits = ["Apel", "Mangga", "Pisang"]
otherFruits = ["Durian", "Semangka", "Jeruk"]
allFruits = fruits + otherFruits
print(allFruits)  # ['Apel', 'Mangga', 'Pisang', 'Durian', 'Semangka', 'Jeruk']










# ===== 10. Dictionaries =====

# Membuat Dictionaries untuk menyimpan biodata seseorang
firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Mengakses item pada Dictionaries dengan 2 cara
# Cara pertama
print(firstPerson['first_name'])  # Hana
# Cara kedua dengan method "get"
print(firstPerson.get('age'))  # 10

# Mendapatkan semua "keys"
print(firstPerson.keys())  # dict_keys(['first_name', 'last_name', 'age'])

# Mendapatkan semua "values"
print(firstPerson.values())  # dict_values(['Hana', 'Malika', 10])

# Menambahkan item berat badan (weight)
firstPerson['weight'] = 12
print(firstPerson)  # {'first_name': 'Hana', 'last_name': 'Malika', 'age': 10, 'weight': 12}

# Mengubah atau mengupdate value dari item, ada 2 cara
firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Cara pertama
firstPerson['age'] = 15

# Cara kedua dengan method "update"
# Jika key ditemukan maka diupdate, jika belum ada maka ditambahkan
firstPerson.update({"age": 15})
firstPerson.update({"hair_color": "black"})
print(firstPerson)  # {'first_name': 'Hana', 'last_name': 'Malika', 'age': 15, 'hair_color': 'black'}

# Menghapus item dengan method "pop" (wajib menyebut nama "key")
firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}
firstPerson.pop("age")
print(firstPerson)  # {'first_name': 'Hana', 'last_name': 'Malika'}

# Menghapus semua item dengan method "clear"
firstPerson.clear()
print(firstPerson)  # {}














# ===== 11. Functions =====

# Membuat Function baru tanpa Arguments
def belajar_python():
    print("Halo")

belajar_python()  # Halo


# Function dengan satu Arguments "name"
def belajar_python(name):
    print("Halo, Saya %s" % name)

belajar_python("Rizqi")  # Halo, Saya Rizqi


# Function dengan dua Arguments: "name" dan "age"
def belajar_python(name, age):
    print("Halo, Saya %s. Umur saya %d" % (name, age))

belajar_python("Rizqi", 30)  # Halo, Saya Rizqi. Umur saya 30


# Function dengan Arbitrary Arguments "names"
def belajar_python(*names):
    for name in names:
        print("Halo, Saya %s" % name)

# Kita bisa mengirimkan banyak value sekaligus
belajar_python("Rizqi", "Fika", "Yudi")


# Function dengan Keyword Arguments
def belajar_python(name, age):
    print("Halo, Saya %s. Umur Saya %d" % (name, age))

# Tanpa nama "key", urutan harus sesuai (name, age)
belajar_python("Rizqi", 30)  # Halo, Saya Rizqi. Umur Saya 30

# Dengan nama "key", urutan boleh berbeda (age, name)
belajar_python(age=25, name="Fika")  # Halo, Saya Fika. Umur Saya 25


# Function dengan Arbitrary Keyword Arguments
def belajar_python(**student):
    print("Halo, Saya %s. Umur Saya %d" % (student['name'], student['age']))

belajar_python(age=20, name="Rizqi")  # Halo, Saya Rizqi. Umur Saya 20


# Function dengan Default Value untuk Arguments "name"
def belajar_python(name="Alien"):
    print("Halo, Saya %s" % name)

belajar_python()  # Halo, Saya Alien