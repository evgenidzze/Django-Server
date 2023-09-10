import json
import re

import django.core.exceptions
from django.core.validators import validate_email
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.views import View
from rest_framework.views import APIView

from orders.models import MenuItem, Category
from orders.serializers import MenuItemSerializer, CategorySerializer


class ItemAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderJsonView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            user_data = data['userData']
            total_sum = 0
            for item in data['order']:
                item_db = MenuItem.objects.filter(id=item['menuItemId'])
                total_sum += float(item_db.get().price) * item['count']

            if total_sum < 7:
                return JsonResponse({'error': 'Total sum is less than 7£'}, status=400)
            for field_name in ('name', 'lastName', 'email'):
                if len(user_data[field_name]) < 1:
                    return JsonResponse({'error': f'Field {field_name} is required'}, status=400)

            if data['deliveryType'] == 'delivery':
                if len(user_data['address']) < 1:
                    return JsonResponse({'error': 'Field address is required'}, status=400)

            try:
                validate_email(user_data['email'])
            except django.core.exceptions.ValidationError:
                return JsonResponse({'error': 'Enter a valid email address'}, status=400)

            phone_pattern = r'^(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{' \
                            r'5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{' \
                            r'3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?$'
            match = re.match(phone_pattern, user_data['phone'])
            if not match:
                return JsonResponse({'error': 'Enter a valid phone number'}, status=400)
            return JsonResponse(data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
