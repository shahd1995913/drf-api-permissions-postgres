from rest_framework import serializers

from .models import Car

class CarSerlizer(serializers.ModelSerializer):
    
    class Meta :
        
        model = Car

        fields = ('id', 'purchaser' ,'name_car', 'created_at', 'description')