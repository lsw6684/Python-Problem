days = ("Mon", "Tue", "Wed", "Thur", "Fri")  # not []
print(days)

#Let's make object including values and attributes
SeungWon = {
  "name" : "SeungWon",
  "age" : 27,
  "Korean?" : True,
  "fav_food" : ["Pasta", "Pizza", "Chicken", "Yupdduk"]
}
print(SeungWon)
print(SeungWon["fav_food"])

#Adding to Object
SeungWon["handsome"] = True
print(SeungWon)



# Note that the lists implement all of the common and mutable sequence,
# but the tuples implement only common sequence.