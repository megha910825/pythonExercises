navbar_links = ["about", "blog", "contact"]                                 
pages = ["index.html", "entry.html"]                                                                                                          

design = [[navbar_links for p in pages] for website in range(4)]                                                                                           

total_links = 0                                                                  
for website in design: 
    for page in design[0]:                                                 
        for link in design[0][0]:                                           
            total_links += 1                                                     

print(total_links) 