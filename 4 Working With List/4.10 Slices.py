n = int(input("Masukkan panjang baris! "))
numbers = list(range(1,n))  # Membuat list dari 1 hingga 20

# Menghitung panjang list
n = len(numbers)
print(n)

# Menentukan nilai tengah
if n % 2 == 0:  # Jika panjang list genap
    mid_index = n // 2
    middle_values = numbers[mid_index - 1:mid_index + 2]  # Mengambil tiga nilai tengah
else:  # Jika panjang list ganjil
    mid_index = n // 2
    middle_values = numbers[mid_index - 1:mid_index + 2]  # Mengambil tiga nilai tengah

print("Nilai tengah:", middle_values)