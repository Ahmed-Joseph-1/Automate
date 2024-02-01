# Automate make it easy
#### Video Demo: https://youtu.be/0zIVmTMWPQE?feature=shared
#### Description:

Do you want to know what this program does? Okay, let's get down to business. 

The program consists of four basic things: 

1. The first function is to extract text from web pages. 

You can extract any text from any web page with a few simple steps: 

* Get the link of the page.
* Then run the program with the `-t` or `--text` argument, for example

Input 
python project.py -t <your url>
output
<website name> saved. 

* The program supports non-Latin languages such as Arabic and Persian.
* The output will be saved in a text file named after the website from which you got the page. 

2. The second function is to extract images from Google search. 

You can extract images from Google Images by doing this: 

* Run the program with the `-i` or '--image' argument, followed by the thing you want to search for, for example 

Input 
python project.py 'i' <your query>
output
Images Downloaded to <your query>_Images. 

* It  will load up to 20 images and create a folder named `(your search term)_Images`.
* It loads the images from Google's servers, so the images are of somewhat poor quality. 

3. The third function is to download images from HTML pages. 

The difference between this function and the previous one is that it loads the images from the pages, not from Google search, so the images retain their quality. 

How do you do this? Just run the program with the `-h` or `--html-image` argument, followed by the link to the page from which you want to download the images, for example 

Input 
python project.py -h <your page url>
output
Images Downloaded to  <website name>_Images.
The images will be saved in a folder named `(images_name of the website from which you got the page)`, like the previous function. 

The tool that loads the images in the second and third functions is `curl`, so you must install it beforehand if you don't have it, or you can go into the source code and change the download method like  'wget' or anything else. 

How to install curl?
installing curl for linux run 
sudo apt install curl
installing curl for termux
pkg install curl 

4. The fourth function is to search within multiple sites. 

For example, you can search for a solution to programming problems within GitHub, Reddit, and Stack Overflow at the same time. 

Just do this: 

* Run the program with the `-s` or `--site` argument.
* Then, the term you want to search for, for example
Input
python project.py -s <your query>
output
All done, you will be redirect
   ed to your browser 
If you are using Termux on an Android mobile, you will be redirected to the browser. Currently, it does not support other systems, but if you want that, you can let me know. 

The default sites are in the `websites.txt` file, which are: 

* GitHub
* Stack Overflow
* Reddit 

You can change them if you want. That's all. 

If you encounter any problems, do not hesitate to contact me. 

**Additional notes:**
* The program use requests library under Apache-2.0 License
* The program use html-text library under MIT License
* The program is written in Python.
* The program is still under development.


