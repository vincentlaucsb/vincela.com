from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
       
class FillInTheBlank(models.Model):
    question = models.TextField()
    id_name = models.CharField(max_length=50)
    answer = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    explanation = models.TextField()
    
    def __str__(self):
        return self.id_name

''' 
    choices:    Each possible choice should be separated by four dashes, e.g. "----"
    answer:     Should be index of correct answer (0, 1, 2...)
'''
class MultipleChoice(models.Model):
    question = models.TextField()
    id_name = models.CharField(max_length=50)
    choices = models.TextField()
    answer = models.IntegerField()
    category = models.ForeignKey(Category)
    explanation = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.id_name