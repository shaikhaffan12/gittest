l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28] 
odd = []
even = []
new_l = []

odd = l1[1::2]
even = l2[0::2]
new_l = odd + even
print(odd)
print(even)
print(new_l)

