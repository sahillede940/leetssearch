scraped_links = []
#read the Leetcode_all_links file and store all links in list
with open("Leetcode_all_links.txt", "r") as file:
    for line in file:
        scraped_links.append(line)


scraped_links = list(set(scraped_links))  #removes duplicate links
print("Inital Data Size:")
print(len(scraped_links))

#Some links present in our scraped data are of solutions we need to remove those links from our scraped data
#this functions helps to remove those links using a fixed pattern present in all solution links
def remove_pattern(arr, pattern):
    req_links = []
    for line in arr:
        if pattern not in line:
            req_links.append(line)
        else:
            pass
    return req_links


Questions_links = remove_pattern(scraped_links, "/solution")
print("Final Data Size:")
print(len(Questions_links))


#Stores the Questions Links data to a Text file
file_path = "Leetcode_questions_links.txt"
with open(file_path, "a") as file:
    for link in Questions_links:
        file.write(link)
