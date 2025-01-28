first_name= "Surya"
middle_name ="Dwi"
last_name="Satria"
full_name=f" {first_name} {middle_name} {last_name} "
print(f"'{full_name}'-> default")
print(f"'{full_name.rstrip()}' -> rstrip()") # rstrip() untuk menghapus whitespace di kanan kalimat
print(f"'{full_name.lstrip()}' -> lstrip()") # lstrip() untuk menghapus whitespace di kiri kalimat
print(f"'{full_name.strip()}'  -> strip()")  # strip()  untuk menghapus whitespace di kiri dan kanan kalimat

