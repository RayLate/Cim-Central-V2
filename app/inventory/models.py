from django.db import models
# Create your models here.


class DeviceType(models.Model):
    name = models.CharField(max_length=30,null=False)
    
    def __str__(self):
        return self.name

class DeviceModel(models.Model):
    name = models.CharField(max_length=30,null=False)
    deviceType = models.ForeignKey(DeviceType,on_delete = models.CASCADE,null=False,default='testing')

    def __str__(self):
        return self.name

class Device(models.Model):
    deviceType = models.ForeignKey(DeviceType, on_delete = models.CASCADE,null=False)
    deviceModel = models.ForeignKey(DeviceModel, on_delete = models.CASCADE,null=False)
    site_choices = [
        ('F10N','F10N'),
        ('F10W','F10W'),
        ('F10A','F10A'),
        ('F10X','F10X'),
        ('MSB','MSB'),
    ]
    site = models.CharField(max_length=5,choices=site_choices,null=True)
    ownership_choices = [
        ('Primary Device','Primary Device'),
        ('Secondary Device','Secondary Device'),
        ('Share Device','Share Device'),
        ('VIP Device','VIP Device'),
    ]
    ownership = models.CharField(max_length=20,choices=ownership_choices,default='Primary Device')

    serialnumber = models.CharField(max_length=15,unique=True,null=False)
    deviceOwner = models.CharField(max_length=10,null=False)
    submittor = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remarks = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.deviceModel} - {self.serialnumber} deployed to {self.deviceOwner} on {self.created_at}'

    def save(self, *args, **kwargs):
        for field_name in ['serialnumber', 'deviceOwner']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self,field_name, val.upper()) # Change attr to upper
        
        return super(Device, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("deployed_success", args=[str(self.id)])
    

