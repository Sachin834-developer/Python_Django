"""
1. Function-Based Views (FBVs)
FBVs are simple Python functions that take an HTTP request and return a response. They are straightforward to use, as they map directly to HTTP methods such as GET, POST, PUT, etc. You define the logic for handling requests inside the function.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
"""
2. Class-Based Views (CBVs)
CBVs are classes that handle HTTP requests by mapping HTTP methods (GET, POST, PUT, etc.) to specific class methods. Django provides a set of built-in generic views that can be extended to handle common tasks, such as creating, retrieving, updating, and deleting objects.

In the context of DRF, CBVs are often used in combination with mixins and generic views to provide a more reusable and modular approach to handling API requests.
"""
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Handles both list, create type of requests
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

"""
Built-In Features: Django and DRF provide a wide range of built-in generic views and mixins for common use cases (e.g., ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView), which reduces the amount of code you need to write.
DRY Principle: CBVs help reduce code duplication by abstracting common patterns into reusable components.
"""

"""
Differences:

FBVs:

Best for simple views that do not require a lot of shared functionality or customization.
More explicit but can lead to repetitive code.
Easier to follow for developers who prefer a more procedural approach.

CBVs:

Best for views that can benefit from reuse, inheritance, and modularity.
More concise and adheres to DRY principles, especially for CRUD operations.
More extensible, allowing developers to customize specific behaviors without rewriting entire views.

Key CBV Components in DRF

Generic Views: These provide built-in views that handle common API patterns such as listing objects, creating objects, retrieving objects, etc. Examples include ListAPIView, CreateAPIView, RetrieveAPIView, and RetrieveUpdateDestroyAPIView.

Mixins: Mixins are reusable pieces of functionality that can be combined with generic views to customize the behavior of the views. Examples include CreateModelMixin, ListModelMixin, and RetrieveModelMixin.

ViewSets: ViewSets are a type of CBV in DRF that allow you to combine multiple actions (e.g., list, retrieve, create, update, delete) into a single class, providing a more RESTful approach to handling requests. ViewSets are commonly used with routers to automatically generate URL patterns.
"""
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
