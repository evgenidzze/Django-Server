from django.urls import path
from django.views.generic import TemplateView

from orders.views import ItemAPIView, CategoryAPIView, OrderJsonView

urlpatterns = [
    path('api/items/', ItemAPIView.as_view()),
    path('api/categories/', CategoryAPIView.as_view()),
    path('api/order-post/', OrderJsonView.as_view()),
    path('test-api/', TemplateView.as_view(template_name='ajax.html'))
]
