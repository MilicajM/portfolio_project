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

    # name that django admin will name itself
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
