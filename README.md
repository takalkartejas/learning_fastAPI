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
5. ASGI provide standard interface between async-capable Python web serves, frameworks and applications
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
3. user model, database and http get requests
   
</summary>

   1. create models.py, this creates a structure to save user data
   2. Add 2 users in main.py
   3. add a funtion to display the user data at localhost:8000/users, check output in browser by refreashing it

</details>

---

## Usefull commands:
<!-- ### 1. Docker images -->
1. uvicorn main:app --reload :- run the application, main is the name of our module, app is the instance of application that we defined, reload:- if any changes are made the server will reload automatically 



