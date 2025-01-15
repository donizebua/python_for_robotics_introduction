name = "Doni" #string

pet_name = "Bobo" #string

luck_number = 71 #integer

decimal = 2.71 #float

shopping_list =['bread', 'milk', 'tv', 'toilet paper', 'truck', 'alphard'] #list
animal_list = ['fish', 'kangaroo', 'horse'] #list
unsur_VIIIA = ('Helium', 'Neon', 'Argon', 'Kripton', 'Xenon', 'Radon', 'Organeson') #tuple
oil = {'coconut oil', 'palm oil', 'peanut oil', 'sesame oil'} #set

my_dictionary = {'name':'Doni', 'pet name': 'Bobo', 'luck number':71} #dictionary

message = "Hello "

# yourName = input("Please input your name! : ")

# print(message + yourName + " From Doni")

# print(shopping_list)
# print(shopping_list*2)
# print(shopping_list[3])
# print(shopping_list[2:4])
# print(shopping_list[:5])
# print(shopping_list[2:])
# print(shopping_list+animal_list)
# print (shopping_list[::-1])
# print (shopping_list[::2])

# print (my_dictionary['luck number'])

# not_found = True

# while not_found:
#     search = input('have you found it yet? : ')
#     if search == 'yes' :
#         not_found = False
#     else: 
#         not_found = True

"iterasi elemen dalam list"
# for items in shopping_list :
#     print(items)

"iterasi dengan index"
# for index, item in enumerate(shopping_list):
#     print(f"{index} : {item}")

"Fungsi enumerate() dalam Python digunakan untuk menambahkan penghitung (index) pada setiap elemen dalam iterable, seperti daftar (list), tuple, atau string. Fungsi ini mengembalikan sebuah objek iterator yang menghasilkan pasangan (index, nilai) untuk setiap elemen dalam iterable."

# fruits = ["apel", "jeruk", "pisang"]

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

"mulai dari 1"
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)


# word = "akusukakamu"
"iterasi string (karakter per karakter)"
# for char in word : 
#     print(char)

"iterasi range angka"
# for i in range(5):
#     print(i)

'dengan range(start, end, step )'
# for i in range (1, 10, 2):
#     print(i)

'iterasi elemen dalam dictionary'
# for key, value in my_dictionary.items():
#     print(f"{key}: {value}")

'iterasi elemen dalam set atau tuple'
# shopping_groups = [['bread', 'milk'], ['tv', 'toilet paper'], ['truck', 'alphard']]
# for group in shopping_groups:
#     for item in group:
#         print(item)

"iterasi dengan kondisi"
# for item in shopping_list:
#     if 't' in item:  # Hanya cetak item yang mengandung huruf 't'
#         print(item)

"break, continue, dan else"
# for item in shopping_list:
#  if item == 'tv':
#     break  # Hentikan loop saat menemukan 'tv'
#     print(item)
#  else:
#     print("Selesai tanpa break")

# for item in shopping_list:
#     if item == 'tv':
#         continue
#     print(item)

"""
Tuple adalah struktur data yang digunakan untuk menyimpan koleksi elemen yang bersifat immutable (tidak dapat diubah setelah dibuat) dan memiliki urutan.
"""

# my_tuple = (1, 2, 3, 4)
# print(my_tuple[1])  # Output: 2

"Tuple dengan elemen berbeda"
# mixed_tuple = (1, "hello", 3.14, True)
# print(mixed_tuple)


"Set adalah struktur data yang digunakan untuk menyimpan koleksi elemen yang bersifat unik (tidak ada elemen duplikat). Set bersifat mutable (dapat diubah) dan tidak ada urutan."
# my_set = {1, 2, 3, 4, 4}  # Elemen '4' hanya disimpan sekali
# print(my_set)  # Output: {1, 2, 3, 4}

"Menambahkan elemen"
# my_set.add(5)
# print(my_set)  # Output: {1, 2, 3, 4, 5}

"Menghapus elemen"
# my_set.remove(3)
# print(my_set)  # Output: {1, 2, 4, 5}

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# print(set1 & set2)  # Output: {3}

# print(set1 - set2)  # Output: {1, 2}

"""Anda bisa membuat kelas yang mendukung iterasi dengan mendefinisikan metode __iter__ dan __next__.
Membuat kelas yang mendukung iterasi memungkinkan Anda menggunakan objek tersebut dalam loop for. Untuk melakukannya, Anda perlu mendefinisikan dua metode utama:
__iter__: Mengembalikan iterator itu sendiri (biasanya self).
__next__: Mengembalikan elemen berikutnya dalam iterasi dan menghentikan iterasi dengan melemparkan StopIteration jika tidak ada elemen lagi."""

'iterator untuk angka'
# class MyNumbers:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self  # Mengembalikan iterator itu sendiri

#     def __next__(self):
#         if self.current <= self.end:
#             num = self.current
#             self.current += 1  # Naikkan nilai
#             return num
#         else:
#             raise StopIteration  # Akhiri iterasi

"Contoh penggunaan"
# numbers = MyNumbers(1, 5)  # Iterasi dari 1 ke 5
# for num in numbers:
#     print(num)


'iterator untuk string'
# class StringIterator:
#     def __init__(self, text):
#         self.text = text
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.text):
#             char = self.text[self.index]
#             self.index += 1
#             return char
#         else:
#             raise StopIteration

"Contoh penggunaan"
# my_string = StringIterator("Python")
# for char in my_string:
#     print(char)


'iterator dengan kondisi khusus'
# class EvenNumbers:
#     def __init__(self, max_num):
#         self.current = 0
#         self.max_num = max_num

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current <= self.max_num:
#             num = self.current
#             self.current += 2  # Lompat ke bilangan genap berikutnya
#             return num
#         else:
#             raise StopIteration

"Contoh penggunaan"
# evens = EvenNumbers(10)  # Bilangan genap hingga 10
# for even in evens:
#     print(even)


'iterasi ganjil'
# class OddNumbers:
#     def __init__(self, start, end):
#         self.current = start if start % 2 != 0 else start + 1  # Mulai dengan angka ganjil
#         self.end = end

#     def __iter__(self):
#         return self  # Mengembalikan iterator itu sendiri

#     def __next__(self):
#         if self.current <= self.end:
#             num = self.current
#             self.current += 2  # Menambahkan 2 untuk mendapatkan angka ganjil berikutnya
#             return num
#         else:
#             raise StopIteration

"Penggunaan"
# numbers = OddNumbers(1, 10)
# for num in numbers:
#     print(num)

"self.current = start if start % 2 != 0 else start + 1 -> ini disebut ternary operator"

'menggunakan yield untuk membuat generator.'
# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count  # Menghasilkan angka satu per satu
#         count += 1

# for num in count_up_to(5):
#     print(num)

"Membuat Iterasi Berdasarkan Waktu atau Kondisi Lain"
# import time

# class DelayedNumbers:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current <= self.end:
#             num = self.current
#             self.current += 1
#             time.sleep(1)  # Menunggu 1 detik antara setiap angka
#             return num
#         else:
#             raise StopIteration

# for num in DelayedNumbers(1, 5):
#     print(num)

"""Python menyediakan pustaka itertools untuk manipulasi iterasi yang lebih canggih. Ini memungkinkan Anda untuk membuat iterasi yang lebih fleksibel tanpa harus menulis banyak kode.

itertools.count(): Menghasilkan angka berurutan mulai dari angka tertentu.
itertools.cycle(): Mengulang elemen dari iterasi tanpa batas.
itertools.islice(): Mengambil irisan dari iterator.
itertools.chain(): Menggabungkan beberapa iterasi menjadi satu."""

import itertools

# for num in itertools.count(5):
#     if num > 10:
#         break
#     print(num)

for item in itertools.cycle(['A', 'B', 'C']):
    print(item)
#     if item == 'C':  # Berhenti setelah satu putaran
#         break

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# for item in itertools.chain(list1, list2):
#     print(item)

"""Fungsi zip() memungkinkan Anda untuk menggabungkan beberapa iterator secara bersamaan dan melakukan iterasi paralel, yang sangat berguna dalam banyak kasus."""
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]

# for name, age in zip(names, ages):
#     print(f'{name} is {age} years old')


"""Memanfaatkan __iter__ yang Menghasilkan Iterasi Tak Terbatas"""
# class InfiniteCounter:
#     def __init__(self, start=0):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.current += 1
#         return self.current

# counter = InfiniteCounter(0)
# for i, num in enumerate(counter):
#     print(num)
#     if i == 9:  # Hanya mencetak 10 angka pertama
#         break




