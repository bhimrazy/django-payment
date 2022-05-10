from re import M
from django.db import models

# Create your models here.
class Payment(models.Model):
    METHODS_OF_PAYMENT = [
        ("ESEWA", 'eSewa'),
        ("KHALTI", 'Khalti'),
        ("HBL", 'HBL')
    ]
    
    product_id = models.CharField(max_length=20)
    method = models.CharField(max_length=6,choices=METHODS_OF_PAYMENT,default=None,)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        unique_together = ('method', 'transaction_id',)

    def __str__(self):
        return str(self.pk)