"""
Handling static files in Django is different in local development vs. production environments. This is because, in production, static files need to be served by a web server (e.g., Nginx, Apache) rather than Django itself, for performance and scalability reasons. Here's a breakdown of how to configure static files in both environments:

1. Local Development
In local development, Django's built-in development server can serve static files for you. This is convenient but not suitable for production.

Settings for Local Development:
STATIC_URL: Defines the base URL for serving static files. This is the URL that will be used to access static files in the browser.

STATICFILES_DIRS: A list of directories where Django will search for static files besides the static/ directory of each app.

Development Server: Django automatically serves static files using the development server when DEBUG=True.

What Happens in Local Development:
Django collects and serves static files directly from the defined directories (STATICFILES_DIRS and app-specific static/ directories).
You do not need to run any additional commands to serve static files; Django will handle it automatically.
"""
# settings.py (local development)

DEBUG = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Example directory outside of app-specific static directories
]

"""
2. Production
In production, you should not serve static files through Django. Instead, use a dedicated web server (e.g., Nginx, Apache) or a cloud storage service (e.g., Amazon S3). The collectstatic management command is used to gather all static files into a single directory, which can then be served by the web server.

python manage.py collectstatic

Settings for Production:
STATIC_ROOT: Specifies the directory where collectstatic will collect all static files. This is where your web server will serve static files from.

STATIC_URL: As in development, this defines the base URL for serving static files. In production, this URL might point to a different domain or CDN.

DEBUG=False: Ensure that DEBUG is set to False in production to prevent Django from serving static files and revealing sensitive information.

What Happens in Production:
Django does not serve static files directly. The collectstatic command collects all static files into the STATIC_ROOT directory, and your web server or CDN handles serving them.
This setup improves performance and scalability, as web servers and CDNs are optimized for serving static content.

"""
# settings.py (production)

DEBUG = False

STATIC_URL = '/static/'  # Can also point to a CDN, e.g., 'https://cdn.example.com/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory to collect static files for serving

# Ensure the production server serves files from this directory.

#################################################################################################

# Example of a Full Static File Setup in Production with S3:

# settings.py (production with S3)

DEBUG = False

STATIC_URL = 'https://your-bucket-name.s3.amazonaws.com/static/'

# Define static storage backend
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS S3 settings
AWS_ACCESS_KEY_ID = 'your-access-key-id'
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# collectstatic will upload static files to S3
STATIC_ROOT = None  # Not needed since files are served from S3
