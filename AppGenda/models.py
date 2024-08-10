from django.db import models

class Frequency(models.TextChoices):
    DAY='D','Diaria'
    WEEK='W','Semanal'
    MONTH='M','Mensual'
    YEAR='A','Anual'

class ToDo(models.Model):
    # ToDo list (Just a list of tasks, without a date)
    id= models.IntegerField(primary_key=True)
    userId= models.IntegerField()
    detail= models.CharField(max_length=40)
    done = models.DateTimeField(null=True, blank=True)
    
class ToDoDate(models.Model):
    # Todo list with a timeout date
    id= models.IntegerField(primary_key=True)
    userId= models.IntegerField()
    detail= models.CharField(max_length=40)
    frequency=models.CharField(max_length=1, choices= Frequency.choices)
    freq_data= models.CharField(max_length=5)  
    done = models.DateTimeField(null=True, blank=True)

class Bills(models.Model):
    # Services's bills to be paid. 
    id= models.IntegerField(primary_key=True)
    userId= models.IntegerField()
    detail= models.CharField(max_length=40)
      
