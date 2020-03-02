This application is developed using Python3 and Django2. if any question, contact mary.ma2000@yahoo.com  

You need to follow the steps below to set up  the environment and run it.
1. You need to install  python 3. 

I used python 3.6
Here is the link for how to install python in win10.

https://www.python.org/downloads/release/python-366/ ; (choose one link of Windows x86-64 web-based installer at the end of this page; when installing python don't forget to select "add PYthon to PATH" and "install python for all users")


2. After installing python in win 10,  go to your project folder.  (You can use win10 built-in cmd or powershell)

for example: cd c:\users\yourname\backend\backend  the project folder name is backend. you can put this folder anywhere in your computer as long as you add python to your PATH.
 
then type the following command in your project folder :  
 
pip install -r requirements.txt  

 ( this command will install Django  and some other required libaries for the application )


3. Still in the project folder ,c:\users\yourname\backend\backend

run the following command:

python manage.py runserver  

( after run this command if you see some warning like  "you need to migrate database", ignore it.  There is no need to migrate database )
 
4. Then, go to browser. google chrome.
Type the following in the url bar. 

http://127.0.0.1:8000/

try this into url : http://127.0.0.1:8000/image/12/?grayscale , you can see the grayscale image is called through url parameter ?grayscale.

click "GRAY' and "ORIGIN" on each image to toggle the grayscale and original image.  ( when you mouse over each image, you can see "GRAY" or "ORIGIN" show up on the image for you to toggle to see the grayscale of each image. )

5. In the applicaition  you can click different dimensions to filter the images or click "load more" button to load more pictures.

Every click of "loading more" is 12 pictures.

If any questions , let me know, mary.ma2009@yahoo.com.
 
 