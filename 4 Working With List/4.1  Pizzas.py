pizzas = ["Pepperoni", "Diavola", "Napolitana", "Margherita", "Taco"]

for pizza in pizzas:
    index_pizza = pizzas.index(pizza)  # Mengambil indeks pizza dalam list
    print(f"index saat ini : {index_pizza}")
    next_pizza = pizzas[(index_pizza + 1) % len(pizzas)]  # Menggunakan modulo untuk looping kembali ke awal
    print(f"next Pizza : {next_pizza}")
    print(f"I like eating {pizza} pizza and {next_pizza} pizza.")
    print()

print("I love pizza!")  # Menambahkan statement untuk menambahkan sentimen positif