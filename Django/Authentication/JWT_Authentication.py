"""
3. JWT (JSON Web Token) Authentication
JWT authentication is a stateless, token-based authentication method. Unlike simple token authentication, JWTs are self-contained tokens that include user information and claims in the token payload, signed with a secret key or a public/private key pair.

When to Use JWT Authentication:
Stateless and Scalable APIs: JWTs are ideal for stateless APIs because all the user information needed for authentication is encoded in the token itself, so there's no need for server-side sessions.
Cross-Platform Applications: JWTs are widely used in mobile apps, SPAs, and cross-platform applications where stateless, token-based authentication is preferred.
Third-Party API Integration: JWTs can be shared between multiple services, making them useful when integrating with third-party APIs or microservices architectures.
Example:
A JWT is issued to the user upon login and is included in the Authorization header for each subsequent request:

Authorization: Bearer <your_jwt_token>

Advantages:
Stateless: The server doesn't need to maintain session information, which improves scalability.
Portable: JWTs can be easily shared across services or domains, enabling single sign-on (SSO) and microservices architectures.
Extensible: JWTs can include additional claims, such as roles and permissions, enabling fine-grained access control.
Drawbacks:
Security Concerns: If a JWT is compromised, it can be misused until it expires. JWTs also tend to have a longer lifespan, which can be a security risk. Implementing token revocation is more complex compared to session-based or token-based authentication.
Token Size: JWTs are larger than simple tokens, which can impact performance if the tokens are frequently exchanged.
"""