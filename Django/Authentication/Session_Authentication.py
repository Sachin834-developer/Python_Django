"""
2. Session Authentication
Session authentication uses Django's built-in session framework. It relies on cookies to maintain a user's session across multiple requests. When a user logs in, a session is created on the server, and a session ID is stored in a cookie on the client.

When to Use Session Authentication:
Traditional Web Applications: If you're building a traditional web application with server-rendered pages (e.g., using Django templates), session authentication is a good choice because it integrates well with Django's session management and CSRF protection.
When You Control the Client: Session authentication is effective when you control both the backend and frontend (e.g., a full-stack Django application) since you can handle cookies and CSRF tokens properly.
Example:
A user logs in via a web form, and the server sets a session cookie. Subsequent requests include the session ID in the cookie for authentication.

Drawbacks:
Not Ideal for APIs Consumed by Third-Party Clients: Session authentication doesn't work well for APIs consumed by mobile apps, SPAs, or third-party clients since it requires the client to manage cookies.
Stateful: Unlike token-based authentication, session authentication is stateful, meaning the server needs to store session data, which might be a drawback for scalability.

"""