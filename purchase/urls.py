from django.urls import path, re_path

from purchase.views import PurchaseList

urlpatterns = [
    re_path('^purchases/(?P<username>.+)/$', PurchaseList.as_view()),
]