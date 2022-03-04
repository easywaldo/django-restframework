import re
from django.shortcuts import render
from purchase.serializers import PurchaseSerializer
from purchase.models import Purchase
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework.decorators import action

# Create your views here.


from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Purchase.objects.filter(purchase_user=user)

def api_root(request, form=None):
    return Response({
        'purchase': reverse('purchase-list', request=request, format=format),
    })
 
# class PurchaseCreate(CreateAPIView):
    
#     def post(self, request, *args, **kwargs):
#         print(request.data)
#         serializer = PurchaseSerializer(data=request.data)
#         if (serializer.is_valid()):
#             print("saved...")
#             #serializer.create(serializer.validated_data)
#             serializer.create(serializer.validated_data)
#             serializer.save()
#             print(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         #print(request["purchase_user"])
#         #return self.create(request, *args, **kwargs)

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
    def perform_create(self, serializer):
        serializer_class = PurchaseSerializer
        if serializer.is_valid(raise_exception=True):
            print('valid...')
            ##serializer.create(serializer.validated_data)  ## 저장 역할 수행
            print(serializer.validated_data)
            serializer.save()   ## 저장역할 수행
            
class PurchaseReadModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
    @action(detail=False, methods=['GET'])
    def superuser(self, request):
        qs = self.get_queryset().filter(purchase_user="super_power")
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)    