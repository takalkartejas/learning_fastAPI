# learning_FastAPI

Video link - https://www.youtube.com/watch?v=GN6ICac3OXY&t=647s

---

## Theory

1. FastAPI is asyncronas similar to node.js and express
2. Fast api is just a framework to build API, we need server to serve the API. For that uvicorn is used
3. Uvicorn :- lighting fast ASGI(Asyncronas service gateway interface) server  
4. 
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
<details> 

---

## Usefull commands:
<!-- ### 1. Docker images -->
1. uvicorn main:app --reload :- run the application, main is the name of our module, app is the instance of application that we defined, reload:- if any changes are made the server will reload automatically 



