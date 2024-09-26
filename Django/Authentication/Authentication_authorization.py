"""
1. Authentication:
Authentication is the process of verifying the identity of a user. DRF supports multiple authentication methods out of the box, and you can also implement custom authentication mechanisms.

Common Authentication Methods in DRF:
Token Authentication: Clients include a token in their request headers to authenticate.
Session Authentication: Uses Django's session framework to manage user sessions (used in web applications).
Basic Authentication: A simple method that sends credentials (username and password) with each request (useful for testing, not recommended in production without HTTPS).
OAuth/OpenID Connect: Provides token-based authentication, commonly used for third-party logins (e.g., via Google, Facebook).

2. Authorization (Permissions)
Authorization determines what authenticated users are allowed to do. DRF provides a robust permission system that allows you to control access to your views.

Common Permission Classes:
IsAuthenticated: Only authenticated users can access the endpoint.
IsAdminUser: Only admin users can access the endpoint.
IsAuthenticatedOrReadOnly: Authenticated users can write; unauthenticated users can only read.


3. CORS (Cross-Origin Resource Sharing)
If your API is consumed by clients from different domains (e.g., a front-end application hosted on a different domain), you need to enable CORS. CORS ensures that your API is securely accessible from specific domains.

CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.com",
]
CORS_ALLOW_ALL_ORIGINS = True , to allow access to all domains


4. HTTPS (SSL/TLS)
Always serve your API over HTTPS to protect data in transit. HTTPS ensures that the communication between clients and your API server is encrypted.

Steps to Implement HTTPS:

Obtain an SSL certificate from a Certificate Authority (CA) or use Let's Encrypt for free SSL certificates.
Configure your web server (e.g., Nginx, Apache) to serve your API over HTTPS.
Redirect all HTTP traffic to HTTPS to ensure secure connections.

5. Prevent CSRF (Cross-Site Request Forgery)
DRF automatically provides CSRF protection for session-based authentication. If you’re using SessionAuthentication, make sure that CSRF protection is enabled by including the CSRF token in your requests.

For other authentication methods (e.g., Token or OAuth), CSRF protection is generally not applicable since these are stateless authentication methods.
"""