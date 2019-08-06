from django.db import models
from django.contrib.auth.models import User

# Product Class
class Product(models.Model):

    def __str__(self):
        return self.title
    
    # title
    title = models.CharField(max_length=255)
    
    # url
    url = models.TextField()
    
    # pub_date
    pub_date = models.DateTimeField()
    
    # votes_total
    votes_total = models.IntegerField(default=1)

    # images
    image = models.ImageField(upload_to='images/')
    
    # icon
    icon = models.ImageField(upload_to='images/')    
    
    # Body
    body = models.TextField()
    
    # pub_date_pretty
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def summary(self):
        return self.body[:100]

    # hunter
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    