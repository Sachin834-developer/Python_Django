"""
1. What is REST API?
To understand what is a REST API, let’s, first of all, understand what is an API. An API stands for an application programming interface. It defines how applications or devices can connect to and communicate with each other.

A REST (Representational State Transfer) API is an architectural style for an API that uses HTTP (Hypertext Transfer Protocol) request methods to access and manipulate data over the Internet. The most popular HTTP request methods (which are explained below) are GET, POST, PUT, DELETE, PATCH, HEAD, TRACE, CONNECT and OPTIONS.

One of the examples of when REST APIs are used is when we need to expose back-end systems and data to front-end developers in a standardized format. That's why REST APIs architecture is vital when it comes to building web services that are consumed by a wide range of clients such as browsers, desktop applications and mobile devices.

2. HTTP Methods
HTTP (Hypertext Transfer Protocol) is a protocol that allows communication between clients and servers on the World Wide Web. There exist several dozen different HTTP Methods that can be used for different purposes. The main 9 most popular HTTP Methods are explained below.

2.1. GET Request
The GET request is one of the HTTP methods which in simple words is in charge of grabbing data from a data source. The response from a GET request can contain data such as a list of items, a single item, or even just a status message.

A GET request is a safe and idempotent method, meaning that it can be repeated multiple times without having any side effects because it should only retrieve data, not modify it.

2.2. POST Request
The POST request is used to send data to the server from a client to create a new resource. The data which is sent as part of a POST request is encoded in the body of the request and is not visible in the URL, unlike with a GET request.

2.3. PUT Request
With help of the PUT request, you can update an existing resource. One important thing to keep in mind when you are updating an existing resource via PUT request is that the request body of a PUT request should contain a complete representation of the resource. Even if you want to update one of the several fields of an existing resource, you need to provide a complete representation of the resource and pass it as a request body. Otherwise, the missing fields will be set to NULL, or in some other cases, the request just would fail. If you want to do a partial update of a resource, look at the PATCH HTTP method.

2.5. PATCH Request
Similar to a PUT HTTP request, a PATCH request can be used to update an existing resource. However, the difference between PUT and PATCH is that when sending a PUT request, the body of a request should contain a complete representation of the resource but with a PATCH request you can provide a partial representation of the resource.

2.4. DELETE Request
The DELETE request can be used when you want to delete an existing resource from the server. Usually, you specify a resource that you want to delete by providing an ID of a resource as part of the URL parameter.

2.6. HEAD Request
HTTP HEAD method is used to fetch the request headers that would be returned if a corresponding GET request was made. In other words, the HEAD method is the same as the GET method with the only difference being that it doesn't return the response body when the request was made.

The HEAD method can be very useful because it can save you some bandwidth in situations when you only need to retrieve some metadata about the resource without retrieving the actual resource as part of the response body. The metadata returned by a HEAD request can be used to validate the information about the resource such as Content-Length of the resource, Content-Type, Last-Modified date, etc.

This metadata from the headers can be very handy in situations when you for example just want to check whether the resource actually exists before fetching it or maybe when you just want to see when the resource was modified last time (P.S. imagine if a resource is a big file and you just need to check the date but you don't want to download it).

2.9. OPTIONS Request
HTTP OPTIONS request method can be used to request the available communication options from the server for the target resource.

When a client sends an OPTIONS request to a server, the server would normally include the list of the allowed HTTP methods for the target resource as part of the "Allow" header in the response

Idempotency : idempotent methods are those that can be called multiple times without changing the result beyond the initial application. In other words, making the same request multiple times will have the same effect as making it just once. 

Idempotent methods: GET, HEAD, PUT, DELETE, OPTIONS, TRACE
Non-idempotent method: POST

NOTE : In most cases, you won’t need to explicitly define or override these methods in your DRF views, as HEAD and OPTIONS are handled automatically. However, if you do need to work with them, DRF provides the flexibility to implement them as needed.


STATUS CODES:

Status Code	Meaning	                Category
100	        Continue	            Informational
200	        OK	                    Success
201	        Created	                Success
204	        No Content	            Success
301	        Moved Permanently	    Redirection
302	        Found	                Redirection
304	        Not Modified	        Redirection
400	        Bad Request	            Client Error
401	        Unauthorized	        Client Error
403	        Forbidden	            Client Error
404	        Not Found	            Client Error
405	        Method Not Allowed	    Client Error
409	        Conflict	            Client Error
500	        Internal Server Error	Server Error
502	        Bad Gateway 	        Server Error
503	        Service Unavailable	    Server Error
504	        Gateway Timeout	        Server Error
"""