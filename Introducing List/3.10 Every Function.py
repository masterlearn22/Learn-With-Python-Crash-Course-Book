anime_character= ["Luffy","Isaghi","Naruto","Goku","Saitama","Meliodas"]

print (f"The list of anime characters is:  {", ".join(anime_character)}.(1)") 
# .join () is used to join the elements of the list into a string with a comma and a space in

anime_character[2] ="Rimuru"
# This line changes the third element of the list to "Rimuru".
print (f"The list of anime characters is:  {", ".join(anime_character)}.(2)")

anime_character.append("Zoro")
# This line adds a new element "Zoro" to the end of the list.
print (f"The list of anime characters is:  {", ".join(anime_character)}.(3)")

anime_character.insert(3,"Bakugo")
# This line inserts the element "Bakugo" at the 4th position in the list
print (f"The list of anime characters is:  {", ".join(anime_character)}.(4)")

anime_character.pop()
# This line removes the last element of the list
print (f"The list of anime characters is:  {", ".join(anime_character)}.(5)")

del anime_character[2]
# This line removes the element at the 3rd position in the list
print (f"The list of anime characters is:  {", ".join(anime_character)}.(6)")

anime_character.remove("Goku")
# This line removes the first occurrence of the element "Goku" in the list
print (f"The list of anime characters is:  {", ".join(anime_character)}.(7)")