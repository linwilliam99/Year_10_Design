
showCategories = {
    "sports": 0,
    "volleyball": 1,
    "ninja": 2,
    "fighting": 3,
    "pirate": 4
}
shows = [["", "haikyu", "", "", ""],
         ["", "", "", "", ""],
         ["", "", "", "naruto", ""],
         ["", "", "", "", "one piece"],
         ["", "", "", "", ""]]

category1 = input("Enter category 1")
category2 = input("Enter category 2")

index1 = showCategories[category1]
index2 = showCategories[category2]

if index1 == index2:
    print(shows[index1][index2])
else:
    print(shows[index1][index2] + shows[index2][index1])