from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.db import models

class PremiumEvent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='premium_events/')
    description = models.TextField()
    date = models.DateField(blank=True, null=True)  # Optional date
    location = models.CharField(max_length=255, blank=True)  # Optional location

    def __str__(self):
        return self.title

class PremiumEventImage(models.Model):
    event = models.ForeignKey(PremiumEvent, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='premium_events/gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.event.title}"



class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    bio = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    
    # Socials
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username}'
    
# --------------------------------------------------------------------------#

class Memory(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField()
    image = models.ImageField(upload_to='memory_images/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Member(MPTTModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    spouses = models.ManyToManyField('self', symmetrical=True, blank=True)
    photo = models.ImageField(upload_to='members/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class MPTTMeta:
        order_insertion_by = ['first_name']

    class Meta:
        verbose_name_plural = 'Members'
        ordering = ['first_name', 'last_name']



# class Person(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField(null=True, blank=True)
#     date_of_death = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

#     father = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children_by_father')
#     mother = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children_by_mother')
#     spouses = models.ManyToManyField('self', symmetrical=True, blank=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=10, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.full_name


# Create your models here.
class Gallery(models.Model):
    headline = models.CharField(max_length=255, default='Default Headline')
    subhead =models.CharField(max_length=250)
    image =models.ImageField(upload_to="images/%y")

    def __str__(self):
        return self.headline

class Event(models.Model):
    headline = models.CharField(max_length=255, default='Default Headline')
    subhead = models.CharField(max_length=250)
    image = models.ImageField(upload_to="events/%Y/%m/")
    date = models.DateField()
    category = models.CharField(max_length=100, default='Gatherings')

    def __str__(self):
        return self.headline
    

    
