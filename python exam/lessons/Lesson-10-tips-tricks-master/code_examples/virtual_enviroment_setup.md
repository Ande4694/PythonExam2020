
# Virtual Enviroment setup

* [12. Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)


## Windows

Creating a virtual enviroment called **tutorial-env**

````
    python -m venv tutorial-env
````
Activating the enviroment

**cmd**

````
    C:\> tutorial-env\Scripts\activate.bat
````
**Git Bash**
````
   source tutorial-env/Scripts/activate
````


**Power shell**  
_This is by default not possible_

## Mac

Creating a virtual enviroment called **tutorial-env**
````
    python -m venv tutorial-env
````
Activating the enviroment
````
    source tutorial-env/bin/activate
````

## Leaving the enviroment. 
Simply write:
````
    deactivate
````
and hit enter.   

## 10 minutes exercise

1. Craete a virtual enviroment, and activet it. 
2. Install the module requests in this enviroment.
3. Create a file called script.py
	a. this file should get the content of this [url](https://www.googleapis.com/youtube/v3/videos?id=0JDNCZyaVXM&key=AIzaSyAqMJi5sUllzUPLVe6tbC557Lc_J5CmiFs&part=snippet,contentDetails,statistics,status,topicDetails,player) and print it to console.  
4. Delete the enviroment (but not the file)





