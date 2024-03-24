from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission,IsAuthenticated

class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response({'sucess': "Hurray you are authenticatedd"})
    

class ProductView(APIView):
    def get(self,request):
        category=self.request.query_params.get('category')
        if category:
            queryset=Product.objects.filter(category_category_name= category)
        else:
            queryset=Product.objects.all()
        queryset = Product.objects.all()
        
        serializer=ProductSerializer(queryset, many=True)
        return Response({'count':len(serializer.data),
                         'data':serializer.data
                         })
    

# Create your views here.
#class ProductCategory(APIView):
    