from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory_count=models.IntegerField()
    last_update=models.DateTimeField(auto_now_add=True)
    
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE="B"
    MEMBERSHIP_SILVER="S"
    MEMBERSHIP_GOLD="G"
    MEMBERSHIP_PLATINUM="P"
    MEMBERSHIP_CHOICES=[
       (MEMBERSHIP_BRONZE,"Bronze"),
        (MEMBERSHIP_SILVER,"Silver"),
        (MEMBERSHIP_GOLD,"Gold"),
        (MEMBERSHIP_PLATINUM,"Platinum"),
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=255)
    address=models.TextField()
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_PENDING="P"
    PAYMENT_COMPLETE="C"
    PAYMENT_FAILED="F"
    
    PAYMENT_CHOICES=[
        (PAYMENT_PENDING,"Pending"),
        (PAYMENT_COMPLETE,"Complete"),
        (PAYMENT_FAILED,"Failed"),
    ]
    
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.DecimalField(max_digits=6,decimal_places=2)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_CHOICES,default=PAYMENT_PENDING)
    order_date=models.DateTimeField(auto_now_add=True)
    payment_date=models.DateTimeField(null=True)
    
    
class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    