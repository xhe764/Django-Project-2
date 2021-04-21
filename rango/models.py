from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models. IntegerField(default=0)
    slug = models.SlugField(unique=True)
    liked_by = models.ManyToManyField(User)

    def save(self, *args, **kwargs):
        if self.views >= 0:
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)
            return True
        else:
            return False


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    first_visit = models.DateTimeField(default=timezone.now)
    last_visit = models.DateTimeField(default=timezone.now) 

    def save(self, *args, **kwargs):
        # now = timezone.now()
        if self.views >= 0 and self.first_visit <= self.last_visit <= timezone.now():
            super(Page, self).save(*args, **kwargs)
            return True
        else:
            print("The page is not saved becaused of error(s).")
            return False

    def __str__(self): # For Python 2, use __unicode__ too
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username
