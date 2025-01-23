"""
1. select_related
select_related is used to optimize queries when you are retrieving related objects from a foreign key or one-to-one relationship. It performs a SQL JOIN operation, which retrieves the related object in the same query as the main object, thus reducing the number of database queries.

Use select_related when you are fetching related objects from ForeignKey or OneToOneField relationships and you want to reduce the number of separate queries.
"""


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


# Without select_related
books = Book.objects.all()
for book in books:
    print(book.author.name)  # This would trigger a separate query for each author

# With select_related
books = Book.objects.select_related("author").all()
for book in books:
    print(book.author.name)  # Only one query for both books and authors
"""
Effect: select_related('author') performs a SQL JOIN to fetch the related Author data in the same query, reducing the number of database hits from N+1 queries to just one.
"""

"""
2. prefetch_related
prefetch_related is used for optimizing queries when dealing with ManyToManyField relationships or reverse foreign key lookups. Unlike select_related, which performs a JOIN, prefetch_related retrieves related objects in separate queries and then performs the relationship mapping in Python. This is useful for many-to-many or one-to-many relationships where select_related would not be effective."""


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)


# Without prefetch_related
books = Book.objects.all()
for book in books:
    print(
        book.authors.all()
    )  # This would trigger a separate query for each book's authors

# With prefetch_related
books = Book.objects.prefetch_related("authors").all()
for book in books:
    print(book.authors.all())  # Fetches all authors in a single query


"""
3. annotate
annotate is used to add aggregate values (like sums, counts, averages, etc.) to your querysets. It allows you to perform database-level calculations and include those results in your queryset. This is useful for performing calculations on related data without having to pull all the data into Python and calculate it manually.

Use Case:
Use annotate when you want to add calculated fields to your querysets based on aggregated data from related objects.

"""
from django.db.models import Count


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


# Get the number of books written by each author
authors = Author.objects.annotate(book_count=Count("book"))
for author in authors:
    print(f"{author.name} has written {author.book_count} books")

"""
4.aggregate()
Purpose: Computes a single value from a set of rows. Unlike annotate(), which operates on individual objects, aggregate() returns a dictionary containing the result of the aggregation.
Example:
"""
from django.db.models import Avg
from myapp.models import Book

# Calculate the average price of all books
average_price = Book.objects.aggregate(Avg("price"))
print(f'Average price: {average_price["price__avg"]}')

"""
Key Differences
Scope:

annotate(): Adds fields to each object in the QuerySet.
aggregate(): Returns a single summary value (or multiple summary values in a dictionary).
Output:

annotate(): The result is a modified QuerySet of the original model.
aggregate(): The result is a dictionary of computed values.

Use Cases:

select_related: Use for optimizing ForeignKey and OneToOne lookups by reducing queries with SQL JOIN.

prefetch_related: Use for optimizing ManyToMany and reverse ForeignKey lookups by reducing queries and handling the relationship mapping in Python.

annotate: Use for adding computed fields to querysets based on aggregated data (e.g., counts, sums) to avoid manual calculations in Python.
"""

"""
Example 2.
Yes, `annotate()` in Django is similar to the SQL `GROUP BY` clause in that it allows you to group records based on specific fields and perform aggregate calculations on those groups. 

### How `annotate()` Works Like `GROUP BY`:

- **Grouping**: When you use `annotate()`, Django groups the records by the specified fields (like you would with `GROUP BY` in SQL).
- **Aggregations**: It allows you to perform aggregate functions (e.g., `Count`, `Sum`, `Avg`, etc.) on each group, resulting in a new field for each object in the QuerySet.

### Example Comparison:

Suppose you have a model called `Order` with a field `customer`:

```python
# Using annotate
"""
from django.db.models import Count
from myapp.models import Order

# Annotate to count orders per customer
orders_per_customer = Order.objects.values("customer").annotate(order_count=Count("id"))
"""
# This will yield a result similar to:
# [{'customer': 1, 'order_count': 5}, {'customer': 2, 'order_count': 3}, ...]
```

In SQL, this would look something like:

```sql
SELECT customer, COUNT(*) as order_count
FROM orders
GROUP BY customer;
```

### Summary:

- **`annotate()`**: Adds an aggregation to each grouped object.
- **`GROUP BY`**: Groups records in SQL and allows aggregate functions to be applied.

So, while they aren't exactly the same, they serve similar purposes in their respective contexts!
    """
