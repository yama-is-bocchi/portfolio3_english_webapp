from django.db import models

# Create your models here.

class Word(models.Model): 
    word = models.CharField(max_length=20, verbose_name="英単語") 
    imi = models.CharField(max_length=20, verbose_name="意味") 
    def __str__(self): 
        return self.word,self.imi
