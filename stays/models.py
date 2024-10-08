from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Host model
class Host(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    hosting_years = models.IntegerField(null =True)
    about = models.TextField(max_length=255, blank =True)
    host_pic = models.ImageField(default='default.jpg', upload_to="host_pics")

    # MALE = 'M'
    # FEMALE = 'F'
    # NON_BINARY = 'NB'
    # OTHER = 'O'
    # GENDER_CHOICES = [
    #     (MALE, "Male"),
    #     (FEMALE, "Female"),
    #     (NON_BINARY, "Non-Binary"),
    #     (OTHER, "Other")
    # ]
   
   # gender = models.CharField(
    #     max_length=2,
    #     choices=GENDER_CHOICES,
    #     default=OTHER,
    #     null=True
    # )
    # rating = models.IntegerField(blank=True, null=True)
    
    # superhost = models.BooleanField(default=False) 

    def __str__(self) -> str:
        return f'{self.user.first_name}, {self.user.last_name}'
    
# Stays model
class Stay(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    location = models.CharField(max_length=255)
    host = models.ForeignKey(Host, on_delete=models.PROTECT, related_name='host')
    guests = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    features = models.TextField(max_length=510)
    description = models.TextField(max_length=510)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title



