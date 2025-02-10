names = ["Mama","Nara","Reta"]
names[1] = "Putri"
names.insert(0,"Ayah")
names.insert(2, "Mas Fajar")
names.append("Rapli")

print(f"This is all my invitation guest {names}")

print("Because something else, i have to cancel guest, and make only 2 guest to be my dinner party ")
popped_guest1 = names.pop(0)
popped_guest2 = names.pop(1)
popped_guest3 = names.pop(1)
popped_guest4 = names.pop(2)
print(f"I am really sorry for my guest that i have to cancel {popped_guest1}, {popped_guest2}, {popped_guest3}, {popped_guest4}")
print(f"Here is my last guest {names}")
del names[0]
names.remove("Reta")
print(f"Here is my last guest {names}")



