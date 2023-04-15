url = "https://warrenteer.wordpress.com/2023/03/07/webscrapingexercise/"
from requests_html import HTMLSession

session = HTMLSession()
response = session.get(url)
response.html.render(timeout=20000)

selector = "#post-1309"
result_text = response.html.find(selector)
result_text = [i.text for i in result_text]

# Open a file for writing
with open("output.txt", "w") as file:
    # Write the text content of each element to the file
    for text in result_text:
        file.write(text + "\n")

    # Find all links on the page and write them to the file
    links = response.html.links
    for link in links:
        file.write(link + "\n")

try:
    # Find the first link in the article using XPath
    link = response.html.xpath('/html/body/div[1]/div/div/main/article[1]/div/p/a')[0]

    # Print the text content of the link
    print(link.text)

except IndexError:
    print("No matching element found")
