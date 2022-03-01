from attr import fields
from rest_framework import serializers

from purchase.models import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    '''
    from purchase.serializers import PurchaseSerializer
    from purchase.models import Purchase
    purchase_serializer = PurchaseSerializer(Purchase.objects.first())
    purchase_serializer.data

    purchase_serializer = PurchaseSerializer(Purchase.objects.all(), many=True)
    purchase_serializer.data

    purchase_serializer = PurchaseSerializer(Purchase(purchase_user='waldo', created='None'), many=False)
    '''
    class Meta:
        model = Purchase
        fields = '__all__'
    
    def validate(self, data):
        if data['purchase_user'] == 'admin':
            raise serializers.ValidationError('운영자는 구매 등록 불가합니다.')