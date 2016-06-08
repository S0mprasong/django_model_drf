from __future__ import unicode_literals

from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE,related_name="article",
        related_query_name="article",)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)

class ArticleDetail(models.Model):
    detial = models.CharField(max_length=100)
    article = models.OneToOneField(
        Article,
        on_delete=models.CASCADE,
        primary_key=True,
        null=False,
        related_name="article_detail"
    )
    def __str__(self):              # __unicode__ on Python 2
        return self.detial

    class Meta: 
        ordering = ('detial',)



