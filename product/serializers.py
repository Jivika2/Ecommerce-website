from rest_framework import serializers
from .models import *

        
class QuantityVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuantityVariant
        fields=('variant_name')
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('category_name','slug')
 

       

class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    quantity_type=QuantityVariantSerializer()
    #colorvariant=ColorVariantSerializer()
    class Meta:
        model = Product
        fields=('category','product_name','image','price','description','stock','quantity_type','color_type','size_type')
        