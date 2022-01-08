from django.db import models

class UserAccount(models.Model):
    user_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    cellphone_number = models.CharField(max_length=11)