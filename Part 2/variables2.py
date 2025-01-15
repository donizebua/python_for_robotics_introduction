# phi = 3.141592657
# b = 1
# c = phi + b
# print(c)

# b+=1
# b = b+1
# b-=1
# b*=2
# b/=3
# b//=3
# print(b)

name = 'mia'
age = 20

set_ex = {1,6,7,4,3,4}
list_ex = [8,5,4,6,4]
dict_ex = {'name': name, 'age': age}

# print(f"Name: {dict_ex['name']}, Age: {dict_ex['age']}")

# print(name, age)

# print (list_ex[1], list_ex[2], f"Name : {dict_ex['name']}", f"Age : {dict_ex['age']}" )

# for key, value in dict_ex.items():
#     print(f"{key.capitalize()} : {value}")

'Konversi set ke list:'
# print(list(set_ex)[1])  # Akses elemen indeks 1 setelah dikonversi ke list

# set_ex.add(10)
# print(set_ex)

"""                                     "error jika elemen tidak ada?"
add	-> Menambahkan elemen	               Tidak
remove -> Menghapus elemen tertentu	       Ya
discard -> Menghapus elemen tertentu       Tidak
pop -> Menghapus elemen acak	           Ya (jika set kosong)
clear -> Menghapus semua elemen	           Tidak
"""


"Tambahkan angka 9 hanya jika belum ada"

# if 9 not in set_ex:
#     set_ex.add(9)
#     print("Angka 9 telah ditambahkan.")
# else:
#     print("Angka 9 sudah ada dalam set.")

"Hapus angka 6 hanya jika ada"

# if 6 in set_ex:
#     set_ex.remove(6)
#     print("Angka 6 telah dihapus.")
# else:
#     print("Angka 6 tidak ada dalam set.")

# print(set_ex)  # Output set setelah operasi

"""
List: Memiliki banyak metode seperti append(), remove(), pop(), sort(), dll.
Set: Memiliki metode seperti add(), remove(), pop(), clear(), dll.
Tuple: Terbatas pada metode seperti count() dan index() karena immutability.
Dictionary: Memiliki metode seperti get(), update(), pop(), keys(), dll.
"""