from django.db import models

class Frequency(models.TextChoices):
    DAY='D','Diaria'
    WEEK='W','Semanal'
    MONTH='M','Mensual'
    YEAR='A','Anual'

class User(models.Model):
    user= models.CharField(max_length=15, db_index=True)
    realName= models.CharField(max_length=40)    
    avatar= models.CharField(max_length=20, null=True, blank=True)

class ToDo(models.Model):
    # ToDo list (Just a listapp of tasks, without a date)
    #id= models.IntegerField(primary_key=True)
    user= models.CharField(max_length=15)
    detail= models.CharField(max_length=40)
    done = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.detail
    
class ToDoDate(models.Model):
    # Todo list with a timeout date
    user= models.CharField(max_length=15)
    detail= models.CharField(max_length=40)
    frequency=models.CharField(max_length=1, choices= Frequency.choices)
    freq_data= models.CharField(max_length=5)  
    done = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.detail
    
class ToPay(models.Model):
    # Services's bills to be paid. 
    user= models.CharField(max_length=15)
    detail= models.CharField(max_length=40)

    def __str__(self):
        return self.detail
      
