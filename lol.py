import os
for i in range(10):
	os.system(f"touch {i}")
	print(f"Number of file: {i} was made")

