# Python virtual environment setup
`virtualenv .venv`
# Activate the python virtualenv
`source .venv/bin/activate`
# Installing all the required python packages
`pip install -r requirements.txt`
# Running the server
`python hello.py`
# RESTful link
https://www.tutorialspoint.com/restful/
# Ports
https://en.wikipedia.org/wiki/Port_(computer_networking)

What is REST?
REST stands for REpresentational State Transfer. REST is a web standards based architecture and uses HTTP Protocol for data communication. It revolves around resources where every component is a resource and a resource is accessed by a common interface using HTTP standard methods. REST was first introduced by Roy Fielding in year 2000.

In REST architecture, a REST Server simply provides access to resources and the REST client accesses and presents the resources. Here each resource is identified by URIs/ Global IDs. REST uses various representations to represent a resource like Text, JSON and XML. JSON is now the most popular format being used in Web Services.

HTTP Methods
The following HTTP methods are most commonly used in a REST based architecture.

|GET | Provides a read only access to a resource.|
|PUT | Used to create a new resource.|
|DELETE | Used to remove a resource.|
|POST | Used to update an existing resource or create a new resource.|
|OPTIONS | Used to get the supported operations on a resource.|

RESTFul Web Services
A web service is a collection of open protocols and standards used for exchanging data between applications or systems. Software applications written in various programming languages and running on various platforms can use web services to exchange data over computer networks like the Internet in a manner similar to inter-process communication on a single computer. This interoperability (e.g., between Java and Python, or Windows and Linux applications) is due to the use of open standards.

Web services based on REST Architecture are known as RESTful Web Services. These web services use HTTP methods to implement the concept of REST architecture. A RESTful web service usually defines a URI (Uniform Resource Identifier), which is a service that provides resource representation such as JSON and a set of HTTP Methods.

Creating RESTFul Web Service
In this tutorial, we will create a web service called User Management with the following functionalities −

|Sr.No.|	HTTP Method|	URI|	Operation	|Operation Type|
|------|-------------|-----|------------|---------------|
|1|	GET	|/UserService/users	|Get list of users	|Read Only|
|2|	GET	|/UserService/users/1|	Get User with Id 1	|Read Only|
|3|	PUT	|/UserService/users/2|	Insert User with Id 2	|Idempotent|
|4|	POST|	/UserService/users/2|	Update User with Id 2	|N/A|
|5|	DELETE|	/UserService/users/1|	Delete User with Id 1	|Idempotent|
|6|	OPTIONS|	/UserService/users|	List the supported operations in web service	|Read Only|
