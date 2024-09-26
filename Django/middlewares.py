"""
In Django, middleware is a way to process requests and responses globally before or after they reach the view layer. Middleware is essentially a series of hooks that sit between the web server and your Django views, allowing you to modify requests and responses, enforce security, manage sessions, or even intercept requests for processing.

Middleware functions are executed in the order they are listed in the MIDDLEWARE setting in your settings.py file. Each middleware can process the request when it comes in, and/or the response when it goes out.

Middleware can be used for tasks like:

Modifying the request before it reaches the view.
Modifying the response before it is sent to the client.
Enforcing security, such as preventing Cross-Site Request Forgery (CSRF).
Managing user sessions and authentication.
Handling browser cookies.

How Middleware Works
    1. Request phase: Middleware is executed in the order listed in the MIDDLEWARE setting, and each middleware can inspect or modify the request.
    2. View phase: The appropriate view function is called.
    3.Response phase: After the view returns a response, the middleware is executed in reverse order (from bottom to top), and each middleware can inspect or modify the response before it's returned to the client.


Some Default Middlewares:

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

1.SecurityMiddleware

This middleware helps manage security-related HTTP headers.
It can enforce HTTPS by redirecting all HTTP requests to HTTPS (using the SECURE_SSL_REDIRECT setting).
It also includes settings like SECURE_HSTS_SECONDS, which enforces HTTP Strict Transport Security (HSTS) for your site.


2.SessionMiddleware

This middleware enables session management in Django.
It adds a session attribute to the HttpRequest object, allowing you to store and retrieve per-user session data.
It works in conjunction with the session backends you configure, such as cookie-based, database-backed, or cache-based sessions.

3.CsrfViewMiddleware

This middleware provides protection against Cross-Site Request Forgery (CSRF) attacks.
It ensures that forms submitted from browsers contain a valid CSRF token.
If the token is missing or incorrect, the request will be rejected with a 403 Forbidden response.

4.AuthenticationMiddleware

This middleware associates users with requests by adding a user attribute to the HttpRequest object.
The user attribute allows you to access the currently logged-in user via request.user in views, templates, etc.
It works with Django's authentication system to manage user logins and sessions.

5.XFrameOptionsMiddleware

This middleware helps prevent clickjacking by setting the X-Frame-Options HTTP header.
By default, it sets the X-Frame-Options header to DENY, which prevents your site from being embedded in a <frame> or <iframe> by other websites.

"""
# Custom Middleware:

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Before view")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("After view")

        return response

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def custom_middleware(self,request):
        print('execute before')

        response = self.get_response(request)

        print('Execute after responsing call')

        return response
    





















