"""

Client Request (HTTP) 
       ↓
  Web Server (e.g., Nginx)
       ↓
  WSGI/ASGI Server (e.g., Gunicorn, Daphne)
       ↓
Django Application
       ↓
  Middleware (Incoming)
       ↓
URL Routing (urls.py)
       ↓
  View Processing (views.py)
       ↓
 Template Rendering (Optional)
       ↓
  Middleware (Outgoing)
       ↓
WSGI/ASGI Server
       ↓
Web Server
       ↓
Client Receives Response


1. The Client Makes a Request
A client (usually a web browser) sends an HTTP request to a Django web application, typically to access a web page or API endpoint.

2. WSGI/ASGI Interface
Django uses a WSGI (Web Server Gateway Interface) or ASGI (Asynchronous Server Gateway Interface) server (e.g., Gunicorn, uWSGI, Daphne) to interface between the web server (e.g., Nginx or Apache) and the Django application.
The WSGI/ASGI server receives the HTTP request from the web server and forwards it to the Django application.

req --> Web server(nginx) --> gateway interface(gunicorn) --> Django application

3. Django Settings and Middleware
The request first passes through Django’s middleware. Middleware is a series of hooks that sit between the request and the view. Middleware can modify the request and response, enforce security policies, manage sessions, etc.
Django applies middleware in the order specified in the MIDDLEWARE setting in your settings.py.
Examples of middleware:

SecurityMiddleware: Enforces security-related HTTP headers.
SessionMiddleware: Manages user sessions.
AuthenticationMiddleware: Associates users with requests.

4. URL Routing
After processing by middleware, Django tries to match the URL of the request to the defined URL patterns in urls.py.
URL patterns are defined using path() or re_path() functions and map specific URLs to corresponding views.

5. View Handling
The view function or method processes the request. This is where the core business logic of your application is handled.
The view interacts with models to fetch or update data, process forms, and perform other tasks as needed.
The view typically prepares a response by rendering a template, returning JSON data (for APIs), or performing a redirect.

from django.shortcuts import render

def my_view(request):
    context = {'message': 'Hello, world!'}
    return render(request, 'my_template.html', context)

7. Returning the Response
Once the view has processed the request and generated the appropriate response (e.g., HTML, JSON, file download, redirect), Django sends the response object back to the middleware.
The response passes through the middleware layers again (this time as an outgoing response), allowing middleware to modify the response (e.g., adding security headers, compressing content).
Finally, the response is sent back to the WSGI/ASGI server, which sends it to the client (e.g., the browser).

8. Client Receives the Response
The client (browser or API consumer) receives the HTTP response from Django.
For web pages, the client renders the HTML content, and for API requests, it processes the JSON/XML data or other content.


"""
