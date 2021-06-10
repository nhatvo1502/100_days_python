row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = float(input("Where do you want to put the treasure? "))
col = int(position/10) - 1
row = int(position%10) - 1
map[row][col]="X"
print(f"{row1}\n{row2}\n{row3}")