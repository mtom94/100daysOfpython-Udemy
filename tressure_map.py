print("Treasure Map")
row1 = ["🟥", "🟥", "🟥"]
row2 = ["🟥", "🟥", "🟥"]
row3 = ["🟥", "🟥", "🟥"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")

#String start with 0th position
#Number start with 1st position

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical-1]
selected_row[horizontal-1] = "#"
#print(horizontal)
#print(vertical)
print(f"{row1}\n{row2}\n{row3}")