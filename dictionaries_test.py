# Copies of dictionaries behave like variables: they get a distinct memory allocation. See the following code snippet:


# >>> dict = {"True": 1, "False": 0}
# >>> copied_dict= dict.copy()
# >>> dict.clear()
# >>> print(copied_dict)
# {'True': 1, 'False': 0}




# A handy way to iterate through both keys and values is the items() method. Can you complete the code in the file colors.py, so that the output would be:


# white = (255, 255, 255)
# blue = (0, 0, 255)
# red = (255, 0, 0)
# green = (0, 128, 0)


colors = {
	"white": (255, 255, 255),
	"blue": (0, 0, 255),
	"red": (255, 0, 0),
	"green": (0, 128, 0)
	}

# Access the colors by key-value pairs
for col,rgb in colors.items():
	print(col,"=",rgb)