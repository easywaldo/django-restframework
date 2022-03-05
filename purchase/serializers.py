from attr import fields
from django.forms import ValidationError
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


    파이선 기본 JSON 변환 사용
    json_str_string = json.dumps(purchase_serializer.data, ensure_ascii=False)
    '{"id": null, "purchase_user": "waldo", "created": "None"}'

    DRF에서 지원하는 JSON 변환 사용 -> 변환 Rule이 추가된 Encoder
    from rest_framework.renderers import JSONRenderer
    json_utf8_string = JSONRenderer().render(purchase_serializer.data)
    b'{"id":null,"purchase_user":"waldo","created":"None"}'

    from rest_framework.response import Response
    response = Response(purchase_serializer.data)
    response.data
    {'id': None, 'purchase_user': 'waldo', 'created': 'None'}
    '''
    class Meta:
        model = Purchase
        fields = '__all__'
    
    def validate(self, data):
        """
        object level validation
        """
        print('validate')
        print(data)
        if data.get('purchase_user') in ['admin', 'big boss']:
            raise ValidationError('운영자는 구매 등록 불가합니다.')
        
        return data
    
    # def validate_purchase_user(self, value):
    #     """
    #     field level validation
    #     필드 레벨 수준과 오브젝트 수준은 함께 사용하지 못한다
    #     """
    #     if 'big boss' in value:
    #         raise ValidationError('운영자는 구매 등록 불가합니다')
    #     return value
        
    # def to_internal_value(self, data):
    #     if data['purchase_user'] == 'admin':
    #         print('validation error')
    #         raise serializers.ValidationError('운영자는 구매 등록 불가합니다.')
    #     return data