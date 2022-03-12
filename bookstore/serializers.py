from rest_framework import serializers

from bookstore.models import Author

class AuthroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'