from django.db import models

class ImageData(models.Model):
    media_id = models.CharField(max_length=30, null=True, blank=True)
    user_id = models.CharField(max_length=15)
    tweetlink = models.URLField(null=True, blank=True)
    tweetimage = models.URLField(null=True, blank=True)
    tweet_image_field = models.ImageField(upload_to='images/', null=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id