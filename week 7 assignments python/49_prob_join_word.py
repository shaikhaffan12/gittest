list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"] 
new = []

for i in list1:
  for j in list2:
    new.append(f"{i} {j}")

print(new)