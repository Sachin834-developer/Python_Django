"""
4. OAuth2 Authentication
OAuth2 is a more advanced and secure token-based authentication framework. It allows third-party applications to grant limited access to a user's resources without exposing the user's credentials. OAuth2 is commonly used for social logins (e.g., Google, Facebook) and when APIs need to be accessed by external clients.

When to Use OAuth2 Authentication:
Third-Party Integrations: OAuth2 is ideal when your API needs to be accessed by third-party applications without sharing user credentials. It allows users to grant or revoke access to specific applications.
Social Logins: If you want users to log in to your application using their social accounts (e.g., Google, Facebook, GitHub), OAuth2 is the standard way to implement this.
APIs with Multiple Clients: OAuth2 is suitable when your API will be consumed by various clients (e.g., web, mobile, third-party services) and you need to manage access levels for each client.
Example:
A user authenticates via a third-party provider (e.g., Google) and receives an access token. The client includes this token in the Authorization header for API requests:


Authorization: Bearer <oauth2_access_token>


Advantages:
Fine-Grained Control: OAuth2 allows you to specify scopes (permissions) for what each application can access, providing granular control over user data.
Delegated Access: Users can grant access to their data without sharing credentials, and they can revoke access at any time.
Widely Adopted: OAuth2 is the de facto standard for authorization, supported by many major platforms and APIs.

Drawbacks:
Complexity: Implementing OAuth2 can be complex, especially when dealing with multiple grant types, token lifecycles, and refresh tokens.
Overkill for Simple Applications: For small projects with limited authentication needs, OAuth2 might be too complex compared to simpler methods like Token or JWT authentication.
"""

"""
Choosing the Right Authentication Method:

Use Token Authentication if:

You are building mobile apps or single-page applications (SPAs).
Your API needs to be stateless and lightweight.
You don't need advanced features like token revocation or fine-grained access control.


Use Session Authentication if:

You are building a traditional server-rendered web application using Django templates.
Your application relies on Django's session management and CSRF protection.
The client and server are closely integrated (e.g., full-stack Django app).


Use JWT Authentication if:

You need stateless authentication with more complex claims (e.g., roles, permissions).
You are building a scalable API consumed by multiple clients (e.g., web, mobile).
You want to use a single token across multiple services or domains (e.g., for single sign-on or microservices).


Use OAuth2 Authentication if:

Your API needs to be accessed by third-party applications (e.g., social logins).
You want to provide fine-grained access control and allow users to delegate access to their data.
You are building a system with multiple clients (e.g., web, mobile) that require secure, delegated access to user resources.

Token Authentication :  
Usecase:         Stateless APIs, Mobile apps, SPAs 
Advantage:       Simple, lightweight, easy to implement
Drawbacks:       Requires client-side token storage, limited security features

Session Authentication:
        Traditional web apps (server-rendered), where you control the client
        Integrated with Django's session management, CSRF protection
        Not ideal for mobile apps, SPAs, or third-party clients, requires server-side session management

JWT Authentication:
        Stateless APIs, cross-platform apps, microservices
        Stateless, scalable, self-contained tokens with claims
        Token revocation is complex, security risks if tokens are not handled properly

OAuth2 Authentication:
        Third-party integrations, social logins, APIs with multiple clients
        Fine-grained access control, delegated access, widely adopted standard
        Complex to implement, overkill for simple use cases
"""