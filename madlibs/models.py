import jsonfield as jsonfield
from django.db import models

# Create your models here.
class Story(models.Model):

    def __str__(self):
        return self.story_title

    story_title = models.CharField(max_length=200)
    story_text = models.CharField(max_length=10000)
    story_image = models.CharField(max_length=2000, default="https://st2.depositphotos.com/4497765/7454/v/450/depositphotos_74540551-stock-illustration-pow-comic-book-cartoon-expression.jpg")

class Processed(models.Model):

    story_text = jsonfield.JSONField()
    story_words = jsonfield.JSONField()
    story_id = models.IntegerField(null=True)