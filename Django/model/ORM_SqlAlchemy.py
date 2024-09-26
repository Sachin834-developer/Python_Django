"""
Django ORM provides a higher-level abstraction of the database, which makes it easier to perform CRUD (Create, Read, Update, Delete) operations without dealing with SQL syntax directly. It also helps maintain database schema migrations and supports different types of relationships (OneToOne, ForeignKey, ManyToMany) between models.

Key Features of Django ORM:

Model Classes: You define database tables as Python classes (models). Each model class corresponds to a table in the database, and the class attributes represent the table columns.

QuerySets: QuerySets allow you to retrieve, filter, and manipulate data in the database. They are lazy, meaning that no query is executed until you actually evaluate the QuerySet.

Automatic Migrations: Django ORM provides tools for managing schema changes via migrations (makemigrations and migrate commands).

Relationships: Django ORM supports different types of relationships between models, such as One-to-One, One-to-Many (ForeignKey), and Many-to-Many.

Database Agnostic: Django ORM is database-agnostic, meaning you can switch between different relational databases (like PostgreSQL, MySQL, SQLite) without changing your Python code, as long as you stick to the ORM's abstractions.


"""
# Defining a model (equivalent to a database table)
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

# Querying the database using the ORM
products_in_stock = Product.objects.filter(in_stock=True)


"""
What is SQLAlchemy?
SQLAlchemy is a popular SQL toolkit and Object-Relational Mapping library for Python. Unlike Django ORM, SQLAlchemy is independent of any web framework, which makes it more flexible and suitable for a wide range of Python applications. SQLAlchemy provides both an ORM layer and a Core layer, which allows for working with raw SQL if needed.

Key Features of SQLAlchemy:
Declarative ORM: SQLAlchemy's ORM uses a declarative syntax, similar to Django ORM, where you define classes that represent database tables.
SQL Expression Language: SQLAlchemy also provides a Core layer, where you can write SQL queries using Python code, allowing for more complex and customized query generation.
Session Management: SQLAlchemy uses a session system to manage database transactions, which allows for more granular control over how data is committed or rolled back in the database.
Extensibility: SQLAlchemy is highly extensible and can be fine-tuned for specific use cases, making it suitable for complex database interactions.
Explicit Mappings: SQLAlchemy gives you more explicit control over how models are mapped to the database, allowing for more advanced configurations and custom SQL.


"""
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# Defining a model (equivalent to a database table)
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    in_stock = Column(Boolean, default=True)

# Connecting to the database and creating a session
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

# Querying the database using SQLAlchemy ORM
products_in_stock = session.query(Product).filter(Product.in_stock == True).all()

"""
When to Use Django ORM vs. SQLAlchemy

Django ORM: Best suited for standard web applications where Django is the primary framework. It’s a great choice when you want a quick and easy solution with minimal configuration, especially for smaller projects or projects with simpler database needs.

SQLAlchemy: Ideal for complex applications where you need fine-grained control over the database interactions. If you require advanced query optimizations, custom transaction handling, or if you’re working on non-Django Python applications, SQLAlchemy is a better fit.

"""