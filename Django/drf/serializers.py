"""
Serializers are used to convert complex data types, such as Django model instances or querysets, into native Python datatypes that can then be easily rendered into JSON, XML, or other content types. 

Serializers also provide deserialization, which allows parsed data (e.g., JSON or form data) to be converted back into complex types, such as model instances, after validating the incoming data.

Serialization: Converting complex data (e.g., Django models) into Python datatypes, which can be easily converted into JSON, XML, etc.

Deserialization: Converting incoming data (e.g., JSON) into Python objects (e.g., model instances) after validating it.
"""
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    published_date = serializers.DateField()

# Example data
book_data = {
    "title": "Django for Beginners",
    "author": "William S. Vincent",
    "published_date": "2020-01-01"
}

# Serialization
serializer = BookSerializer(data=book_data)
if serializer.is_valid():
    print(serializer.data)  # Serialized data (Python native types)
else:
    print(serializer.errors)

# Deserialization
deserialized_book = serializer.save()  # This would typically create or update an instance

"""
Validation in Serializers:

You can add custom validation logic in serializers at both the field level and the object level.
"""
# Field-Level Validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("The title must contain the word 'Django'")
        return value

# Object-Level Validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['author'] == "Anonymous" and data['published_date'] > datetime.date.today():
            raise serializers.ValidationError("Anonymous authors cannot publish future books.")
        return data
