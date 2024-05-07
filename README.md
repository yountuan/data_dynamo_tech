Since we were allowed to do any project by our Dean, I developed a CRM for shop inventory. Technology used: Django Rest Framework, JWT Authentication, Web Sockets, Docker Compose, Swagger Documentation, Render Server, Git,

Deploy in Free Render Server;

Web service backend deploy: https://store-8r6h.onrender.com
Video explanation: https://drive.google.com/drive/folders/1BR_qLzhz5P1JVFfpLAKOqZHvO-NuY4hR?usp=sharing


More explained in Video presentation.
In the main page you will just see ERROR 404 Because first of all, I dont have anything in landing page, and second of all, I turned Debug=False, so that other people will not see logs unless you are a developer that works on this project. And if you make Debug=True, you can see this log page which shows existing urls.![In the main page you will just see ERROR 404 Because I turned off Debug=True, so that other people will not see logs unless you are a developer that works on this project.](<images/Screenshot 2024-05-08 at 02.15.15.png>) 
Both Database and Backend APIs containerized in Docker compose, deployed and available on server.
![alt text](<images/Screenshot 2024-05-08 at 02.15.46.png>)
You can see and also manage store's data in admin-pannel. You can see which tables are there in my project.
![alt text](<images/Screenshot 2024-05-08 at 02.16.06.png>)
![alt text](<images/Screenshot 2024-05-08 at 02.16.18.png>) 
![alt text](<images/Screenshot 2024-05-08 at 02.16.37.png>) 
![alt text](<images/Screenshot 2024-05-08 at 02.16.54.png>)
There are added Web sockets so that you can check how requests work using GUI.
![alt text](<images/Screenshot 2024-05-08 at 03.06.12.png>)

You can check all of api's and requests in Postman.
![alt text](<images/Screenshot 2024-05-08 at 02.18.10.png>) 
You can see in the pictures above the tables in both Store and Account app. It is shown below which fields you should fill and which data types they should be.
And if could notice you should authenticate with JWT token which you can obtain from endpoints.