from django.shortcuts import render
from purchase.serializers import PurchaseSerializer
from purchase.models import Purchase
# Create your views here.


from rest_framework import generics

class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Purchase.objects.filter(purchase_user=user)