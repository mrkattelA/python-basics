my_dict={2:1,3:2,4:3,5:4}
i=0
print("{")
for k,v in my_dict.items():
	print("  ",k,":",v, end="")
	i=i+1
	if i<len(my_dict):
		print(",")
print("\n}")