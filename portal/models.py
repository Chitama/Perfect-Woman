from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)




class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(blank=True, null=True, max_length=256)
    brand = models.CharField(blank=True, null=True, max_length=256)
    product_img = models.CharField(blank=True, null=True, max_length=256)
    Component = models.CharField(blank=True, null=True, max_length=128)
    registered = models.DateField(blank=True, null=True, max_length=16)

    def __str__(self):
        return self.product



class Component(models.Model):
    id = models.AutoField(primary_key=True)
    Component = models.CharField(blank=True, null=True, max_length=256)
    registered = models.DateField(blank=True, null=True, max_length=16)

    def __str__(self):
        return self.component


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_type = models.CharField(blank=True, null=True, max_length=32)
    category_id = models.CharField(blank=True, null=True, max_length=32)
    category = models.CharField(blank=True, null=True, max_length=128)
    order = models.CharField(blank=True, null=True, max_length=8)
    registered = models.DateField(blank=True, null=True, max_length=16)

    def __str__(self):
        return self.category
