import random

# Membuat list_1 dengan 10 angka acak dalam rentang 20-40
list_1 = [random.randint(20, 40) for _ in range(10)]
# Menghitung rata-rata dari list_1
avg_list_1 = sum(list_1) / len(list_1)

# Membuat list_2 dengan 20 angka acak dalam rentang 20-60
list_2 = [random.randint(20, 60) for _ in range(20)]
# Menghitung rata-rata dari list_2
avg_list_2 = sum(list_2) / len(list_2)

# Menentukan kategori untuk rata-rata list_2
def evaluate_average(avg):
    if 20 <= avg < 40:
        return "Normal"
    elif 40 <= avg < 50:
        return "Kurang Bagus"
    else:  # 50-60
        return "Buruk"

# Evaluasi rata-rata list_2
evaluation = evaluate_average(avg_list_2)

# Menampilkan hasil
print(f"List 1: {list_1}")
print(f"Rata-rata List 1: {avg_list_1:.2f}\n")

print(f"List 2: {list_2}")
print(f"Rata-rata List 2: {avg_list_2:.2f}")
print(f"Evaluasi: {evaluation}")
