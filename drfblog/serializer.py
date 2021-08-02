from rest_framework import serializers

from .models import Blog


class BlogPostSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = Blog
        fields = '__all__'



