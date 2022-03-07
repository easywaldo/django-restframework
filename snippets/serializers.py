from django.forms import ValidationError
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
class UserSerializer(serializers.HyperlinkedModelSerializer):
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    
    # 직접 필드설정하여 시리얼라이징
    #owner = serializers.ReadOnlyField(source='owner.username')
    
    # 중첩 시리얼라이저 방식
    owner = UserSerializer()
    
    highlighted = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlighted', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']
        
    def validate(self, data):
        if data.get('code') in ['basic', 'cobol']:
            #raise serializers.ValidationError('해당 코드는 등록 불가합니다.')
            raise ValidationError('해당 코드는 등록 불가합니다.')
        
        return data
        
class CustomSnippetSerializer(serializers.Serializer):
    class Meta:
        fields = ['title', 'code', 'style', 'owner']