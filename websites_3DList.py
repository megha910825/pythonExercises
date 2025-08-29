# Open the file website.py, and create a 3D list with the navigation bar items for each page index.html, blog.html and contact.html, for a total of four websites. 
# Iterate over this 3D list to calculate how many navigation bars in total need to be designed.

navbar_links = ["about", "blog", "contact"]                                 
pages = ["index.html", "entry.html"] 
# row = nav for nav in navbar_links
websites=[[navbar_links  for page in pages] for row in range(4)]
# Create the 3D array here

print(websites)
total_links = 0
for i in range(4):
    for j in range(3):
        for k in range(2):
           total_links= total_links+ 1
        
# Iterate over the 3D array




print("total number of links:", total_links)