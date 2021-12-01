from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Car(models.Model):

    purchaser  =  models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    name_car = models.CharField(max_length=64)
    
    description  = models.TextField()
   
    created_at = models.DateTimeField(auto_now_add= True)

    updated_at = models.DateTimeField(auto_now= True)
 


    def __str__(self):
        return self.name_car