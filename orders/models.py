from django.db import models
from django.contrib.auth.models import User
from products.models import Item 
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),
    ]

    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    tot_amount=models.DecimalField(max_digits=8,decimal_places=2)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order #{self.id} by {self.customer.username}"


class OrderItem(models.model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity_ordered=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity_ordered}*{self.item.name}"

        

