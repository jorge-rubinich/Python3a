from django.contrib import admin
from AppGenda.models import ToDo, ToDoDate, ToPay

# Register your models here.
admin.site.register(ToDo)
admin.site.register(ToDoDate)
admin.site.register(ToPay)