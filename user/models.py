from django.db import models

class User(models.Model):
    
    user_name = models.CharField(max_length=20)
    user_type = models.IntegerField() # 0: 사용자, 1: 사장님

    def __str__(self):
        return 

    def __unicode__(self):
        return 
