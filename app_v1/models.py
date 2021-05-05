from django.db import models


class Order(models.Model):
    PAYMENT_STATUS = [
        ('C', 'CREATED'),
        ('P', 'PAYED'),
        ('R', 'REJECTED'),
    ]
    customer_name = models.CharField(max_length=80, null=False)
    customer_email = models.EmailField(max_length=120, null=False)
    customer_mobile = models.CharField(max_length=40, null=False)
    status = models.CharField(max_length=1, choices=PAYMENT_STATUS, null=False, default='C')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Order id: {self.id}'

    class Meta:
        db_table = 'orders'
