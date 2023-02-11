from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name="%(class)s_createdby",
        on_delete=models.CASCADE,
        null=True)
    upated_by = models.ForeignKey(
        User, related_name="%(class)s_updatedby",
        on_delete=models.CASCADE,
        null=True
    )
    
    class Meta:
        abstract = True

class Site(BaseModel):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=False)
    zipcode  = models.IntegerField(null=False)

    def __str__(self):
        return self.site_name

class IAP(BaseModel):
    serial_number = models.IntegerField(primary_key=True)
    mac_address = models.CharField(max_length=50, null=False)
    ip_address = models.CharField(max_length=30, null=False)
    model = models.CharField(max_length=20, null=False)
    status = models.CharField(max_length=20, name=False)
    is_VC = models.BooleanField(null=False)
    site_id =models.CharField(max_length=20, null=False)
    site_id=models.ForeignKey(Site, related_name='IAP_site', on_delete=models.CASCADE)
    
class switch(BaseModel):
    serial_number = models.IntegerField(primary_key=True)
    mac_address = models.CharField(max_length=50, null=False)
    ip_address = models.CharField(max_length=30, null=False)
    model = models.CharField(max_length=20, null=False)
    status = models.CharField(max_length=20, name=False)
    is_VC = models.BooleanField(null=False)
    site_id=models.ForeignKey(Site, related_name='switch_site', on_delete=models.CASCADE)

class Order(BaseModel):
    order_id = models.IntegerField(primary_key=True)
    purchase_id = models.IntegerField(primary_key=False)
    csm_name = models.CharField(max_length=100,null=False)
    status = models.CharField(max_length=100, null=False)