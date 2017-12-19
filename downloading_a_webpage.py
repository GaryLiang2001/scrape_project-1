from urllib.request import urlopen

url = "https://search.jd.com/Search?keyword=titan%20v&enc=utf-8&suggest=4.def.0.V09&wq=titan&pvid=d0474b74b7f24725bc487c541b693151"

def get_webpage(url):

	print("Getting Request Object")
	request = urlopen(url)
	print("Reading Request Object")
	data = request.read()
	text = data.decode("utf-8")

	print("Web Page Downloaded")
	return  text

text = get_webpage(url)

with open('html_text.txt', 'w') as f:
	f.write(text)