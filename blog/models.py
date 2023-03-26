from django.db import models

# Create your models here.
# title
# publication date
# body
# image


class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


# add the blog app

# create a migration

# migrate

# add to the admin
