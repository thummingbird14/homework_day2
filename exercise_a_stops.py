stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
print(stops)
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0,"Glasgow Queen St")
print(stops)
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4,"Polmont")
print(stops)
#4. Print out the index position of "Linlithgow"
Lin_index = stops.index("Linlithgow")
print(Lin_index)
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
print(len(stops))
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop
