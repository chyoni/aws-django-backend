from django.db import models

class Shop(models.Model):

    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)

    def __str__(self):
        return 

    def __unicode__(self):
        return 

class Menu(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)

class Order(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    address = models.CharField(max_length=40)
    estimated_time = models.IntegerField(default=-1)
    delivery_finish = models.BooleanField(default=False)


class Orderfood(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)
