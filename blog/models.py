from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_date = models.DateTimeField()
    post_text = models.CharField(max_length=300)
    post_fulltext = models.CharField(max_length=1500, null=True)
    post_image = models.ImageField(upload_to='post_images/')

    def get_summary(self):
        return self.post_text[:65]

    def __str__(self):
        return self.post_title
