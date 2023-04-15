url = "https://warrenteer.wordpress.com/2023/03/07/webscrapingexercise/"
from requests_html import HTMLSession

session = HTMLSession()
response = session.get(url)
response.html.render(timeout=20000)

selector = "#post-1309"
result_text = response.html.find(selector)
result_text = [i.text for i in result_text]

print(result_text)
