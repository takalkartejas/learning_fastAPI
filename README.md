# learning_FastAPI

Video link - https://www.youtube.com/watch?v=GN6ICac3OXY&t=647s

---

## Theory

1. FastAPI is asyncronas similar to node.js and express
2. Fast api is just a framework to build API, we need server to serve the API. For that uvicorn is used
3. Uvicorn :- lighting fast ASGI(Asyncronas service gateway interface) server  
4. HTTP request methods:
   HTTP defines a set of request methods to indicate the desired action to be performed for given resource. eg. of methods:- get, head 

   https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
5. GET:- The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
6. POST:- The HEAD method asks for a response identical to a GET request, but without the response body. 
7. ASGI provide standard interface between async-capable Python web serves, frameworks and applications
---

## Learning steps:
<details> <summary>
1. Up and running with api
   
</summary>

   1. create main.py and to make simple application to return hello world in form of dictionary
   2. run app using command 1, we get output as-
      ``` bash
      $ uvicorn main:app --reload
      INFO:     Will watch for changes in these directories: ['/home/tejas/study/learning_fastAPI']
      INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO:     Started reloader process [8083] using WatchFiles
      INFO:     Started server process [8085]
      INFO:     Waiting for application startup.
      INFO:     Application startup complete.
      ```
   3. enter localhost:8000 on browser to check output
   4. change the pyhon file and just refresh the page and the changes are reflected

</details>

<details> <summary>
2. HTTP Methods : refer theory 4
   
</summary>

   1. You can do inspect in browser and check the in network the 'get' request
   2. Async and await:- We use this keywords to await for somthing to happen asyncronasly. refer theory 5

</details>

<details> <summary>
3. user model, database 
   
</summary>

   1. user model:- create models.py, this creates a structure to save user data
   2. Database:- Add 2 users in main.py


</details>

<details> <summary>
4. http get requests :- refer theory 5
   
</summary>

   1. Add a funtion to display the user data at localhost:8000/users, check output in browser by refreashing it
   2. If we refresh the browser the uuid changes every time,  We copy the uuid from browser and paste in id to avoid different uuid everytime
</details>

<details> <summary>
5. http post requests :- refer theory 6
   
</summary>

   1. We create a post request inside main.py to add additional user
   2. We will need a client to test the post request
</details>


<details> <summary>
6. Rest client
   
</summary>

   1. Install thunder client extension in vs code
   2. Go to thuder client, click on new request, in get type http://localhost:8000/users, and we get the same json output as we got on browser
   3. copy one of the user model objects from the output of get and then click on new client
   4. In new client select post and got to body, in body select json, paste the object and edit the user properties like name etc. (delete the id part as it will be genrated automatically)
   5. click on send, we get a the generated id in response, this id is retured in the post function in main.py
   6. We then use the same get request as we did before and send, then we see that the new user was automatically added
   7. We can also see on browser that new user is added
   8. If we modify the main.py file then the server reloads and the new user that was added is gone
</details>

<details> <summary>
7. Swaggger docs and redoc
   
</summary>

   1. Type http://localhost:8000/docs on browser we get an interactive documentation.
   2. We can check all the documentation of the API that we created here
   3. We use the post request by using 'tryout' changing the example data and using 'execute'
   4. Then we check the modified data using the get request. 
   5. Type http://localhost:8000/docs on browser we get a non interactive documentation of redoc.
</details>

---

## Usefull commands:
<!-- ### 1. Docker images -->
1. uvicorn main:app --reload :- run the application, main is the name of our module, app is the instance of application that we defined, reload:- if any changes are made the server will reload automatically 



