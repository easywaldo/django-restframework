from django.http import Http404
from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class PurchaseDetailApiView(APIView):
    """
    Retrieve, update or delete a Purchase instance.
    """
    def get_object(self, pk):
        try:
            return Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print('apiview get execution.....')
        user_agent = request.META.get("HTTP_USER_AGENT")
        print(user_agent)
        
        Purchase = self.get_object(pk)
        serializer = PurchaseSerializer(Purchase)
        return Response(serializer.data)

    def put(self, request, pk):
        print(pk)
        purchase = self.get_object(pk)
        print(purchase.purchase_user)
        serializer = PurchaseSerializer(purchase, data=request.data)
        print(request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    
    
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Purchase = self.get_object(pk)
        Purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)