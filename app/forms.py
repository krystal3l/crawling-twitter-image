from django import forms

#models.py에 정의한 ImageData 모델 import
from .models import ImageData

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageData
        fields = ('user_id', 'tweetlink', 'tweetimage', 'tweet_image_field')