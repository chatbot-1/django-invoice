from django.db import models

# Create your models here.

class Client(models.Model):
    comp_name = models.CharField(max_length=50)
    gst = models.IntegerField()
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.comp_name
    
    class Meta:
        db_table = 'clients'
    
class Service(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'services'
    
class Provider(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.TextField()
    account = models.IntegerField()
    ifsc = models.IntegerField()

    def __str__(self):
        return self.comp_name
    
    class Meta:
        db_table = 'providers'

