import requests
import sys
import re
import os
from html_text import extract_text


def main():
	try:
		if sys.argv[1] == "-t" or sys.argv[1] == "--text":
			print(text_extractor(*sys.argv))

		elif sys.argv[1] == "-i" or sys.argv[1] == "--image":
			print(image_extractor(*sys.argv))

		elif sys.argv[1] == "-h" or sys.argv[1] == "--html-image":
			print(html_image_extractor(*sys.argv))

		elif sys.argv[1] == "-s" or sys.argv[1] == "--site":
			print(site_search(*sys.argv))

	except IndexError:
		print("\033[31;m missing operand")
		print("\033[32;m Hint: Read README.md file")

def text_extractor(*args):
	r = requests.get(args[2])
	r.encoding = 'utf-8'
	file = f'{re.search("https://(.+?)/", args[2]).group(1)}'

	with open(file, "w") as f:
		f.write(extract_text(r.text))

	return f"\033[1;32m {file} Saved. \n"


def site_search(*args):
	with open("websites.txt") as f:
		data = f.read()

	websites = re.findall(r'https://(.+)', data)
	new_websites = []

	for domain in websites[:4]:
		url = f'"https://www.google.com/search?q={args[2]}&as_sitesearch={domain}"'
		new_websites.append(url)

	os.system(f'for url in {" ".join(new_websites)} ; do termux-open-url $url & done')

	return "\033[1;32m All done, you will be redirected to your browser \n"


def image_extractor(*args):
	response = requests.get(f"https://www.google.com/search?q={args[2]}&tbm=isch")
	pattern = r'"https://encrypted-tbn0.gstatic.com/.+?"'

	dir_name = f"{args[2]}_Images"
	os.mkdir(f"{dir_name}")

	num = 0
	for url in re.findall(pattern, response.text):
		num += 1
		os.system(f'curl {url} --output "{dir_name}/{num}.jpg"')

	return f"\033[1;32m {num} Images Downloaded to {dir_name}. \n"


def html_image_extractor(*args):
	response = requests.get(args[2])
	pattern = r'"https://[^ ]+?jpg[^ ]*?"'

	dir_name = re.search('https://(.+?)/', args[2]).group(1)
	os.mkdir(f"{dir_name}_Images")

	num = 0
	for url in set(re.findall(pattern, response.text)):
		num += 1
		os.system(f'curl {url} --output "{dir_name}_Images/{num}.jpg"')

	return f"\033[1;32m {num} Images Downloaded to {dir_name}. \n"


if __name__ == "__main__":
	main()
