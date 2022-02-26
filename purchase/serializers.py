from attr import fields
from rest_framework import serializers

from purchase.models import Purchase

class   PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
    
    def validate(self, data):
        if data['purchase_user'] == 'admin':
            raise serializers.ValidationError('운영자는 구매 등록 불가합니다.')