from django.db import models

# Create your models here.

class Testimony(models.Model):    
    name = models.CharField(max_length = 70)
    occupation = models.CharField(max_length = 100)
    message = models.CharField(max_length = 500)
    pic = models.CharField(max_length = 180)

class MostFeaturedArticle(models.Model):
    article_title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 220)
    header_img = models.ImageField(upload_to='article_imgs')

class GeneralArticle (models.Model):
    article_title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 220)
    header_img = models.ImageField(upload_to='article_imgs')

class HallwayEvent(models.Model):
    event_title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 220)
    location = models.CharField(max_length=220)
    flyer_img = models.ImageField(upload_to='hallway_events')
    date = models.DateField()
    time = models.CharField(max_length=50)

class TrendingVendorArticle(models.Model):
    article_title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 220)
    business_name = models.CharField(max_length=120)
    business_profile_pic = models.ImageField(upload_to='business_profile_pic')

class TopPerformingProfessionalArticle(models.Model):
    article_title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 220)
    name_of_person = models.CharField(max_length=120)
    profile_picture = models.ImageField(upload_to='profile_pics')
    
class Team(models.Model):
    name = models.CharField(max_length = 120)
    role = models.CharField(max_length = 200)
    twitter = models.CharField(max_length=400)
    linkedin = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    pic = models.ImageField(upload_to='images/')
    
    
