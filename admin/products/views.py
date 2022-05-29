from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .producer import publish
from .serializers import ProductSerializer
import random



class ProductViewSet(viewsets.ViewSet):
    def list_items(self, request):
        pass 
    
    def create_items(self, request):
        pass 

    def delete_items(self, request):
        pass 
    
    def retrive_items(self, request):
        pass 
    
    def update_items(self, request):
        pass 