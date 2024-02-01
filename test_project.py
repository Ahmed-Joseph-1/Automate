from project import *

url = "https://islamqa.info/en"
url2 = "https://en.m.wikipedia.org/wiki/Islam"

def test_text_extractor():
	assert text_extractor("project.py", "-t", url) == "\033[1;32m islamqa.info Saved. \n"

def test_image_extractor():
	assert image_extractor("project.py", "-i", "islam") == "\033[1;32m 20 Images Downloaded to islam_Images. \n"

def test_html_image_extractor():
	assert html_image_extractor("project.py", "-h", url2) == "\033[1;32m 3 Images Downloaded to en.m.wikipedia.org. \n"

def test_site_search():
	assert	site_search("project.py", "-s", "android") == "\033[1;32m All done, you will be redirected to your browser \n"

