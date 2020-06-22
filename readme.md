## Description	
Express Daily is a full stack blog app which is built on the following tech stack : Angular, Flask, Docker, Postgres, Nginx, Celery and Redis. Lets us understand what is the purpose of each tool/ framework
* **Flask** - provides the API for the apps and describes all the routes of the server to which client submits the request
* **Angular**- provides the client interface such as homepage, add post, login and other basic user functionality.
* **Docker** : provides containers for the each service. App has following services that are all clubbed in one docker-compse file. Frontend, backend, Nginx, Celery, Redis, database.
* **Postgres** : provides the database for the app
* **Celery** : provides functionality for secondary task such as sending reset password link to user's email id and works asynchronously so that server is not blocked when the link is being preapred to be sent to client's email id.
* **Redis** : acts as the message queue for Celery task
* **Nginx**: used as a reverse proxy for both frontend and backednd services. App runs on localhost port 80 and Nginx acts as a door to send proxy request to actual ports of  frontend and backend thus keeping the interaction abstract to the user.

## Features
* Adding a post
* Updating a post
* Deleting a post
* Signing up on the app ( Register)
* Logging into the personal homepage
* Changing the password by sending reset link Async
* O'Auth Authentication
* Includes frontend testing using Jasmine and Karma
* Includes backend testing using Pytest

## How to run the app
* Clone the repo using  
	 `git clone https://github.com/chowdharyniraj97/Blog.git`
	 
* Go to root directory and cd into **BLog** directory and create a myEnvVal.py file and add the following:
	* `os.environ['EMAIL']='<Your-email-id>'
    os.environ['Password']='<your actual password>'
   `
   The above file is important and  mainly used to send the reset password link for the forgot password functionaltiy and this email id will be used by mail server to send an email.
	
* cd into repo and go to client directory and run
	* `npm i`
	
 * cd into root directory(Blog) and run
	 * `docker-compose up --build`
	 
* Open your web browser and navigate to 
	* `http://localhost/`
	
* Register yourself and login into the app and play around

# Extra
Feel free to point out any issues in the app, you can reach out to me at chowdharyniraj97@gmail.com also if app does not run on you machine drop me an email and will try my best to help you and get the app running. Happy coding :D
