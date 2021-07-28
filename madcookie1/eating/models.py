from django.db import models
from django.utils import timezone
# from djangoratings.fields import RatingField
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Eating(models.Model):
    image = models.ImageField(upload_to='eatingimages/', blank=True, null=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='snacks')
    market_date = models.CharField(max_length=20)
    pub_date = models.DateTimeField(default=timezone.now)
    calories = models.CharField(max_length=200)
    information = models.TextField()
    hashtag = models.ManyToManyField('HashTag', blank=True)
    purchase_link = models.CharField(blank=True, max_length=200)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    eating= models.ForeignKey(Eating, on_delete=models.CASCADE)
    score=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    image=models.ImageField(upload_to="reviewimages/", blank=True, null=True)
    body=models.TextField(blank=False)
    pub_date=models.DateTimeField(default=timezone.now)
    salty_taste = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    sweet_taste = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    spicy_taste = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    #건강은 관리자가 직접 설정

    def summary(self):
        return self.body[:100]

class HashTag(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name





