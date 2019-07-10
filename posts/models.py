from django.db import models
from django.contrib.auth.models import User
#from phone_field import PhoneField
#from address.models import AddressField



class Post(models.Model):
    title = models.CharField(max_length=50, null=True )
    #cover = models.ImageField(upload_to='images/' )
    #email = models.EmailField(  max_length=70, null=True)
    #phno = models.PhoneField(blank=True, help_text='Contact phone number')
    #phno = models.CharField(max_length=10, null=True)
    #adrss1 = models.TextField(null=True)
    #adrss2 = models.TextField(null=True)
    #adrss2 = AddressField(null=True)
    #dob = models.DateTimeField(null=True)





    #a = models.ManyToManyField(User, blank="True")

    def __str__(self):
        #return self.title
        return ' {} '.format(self.title)