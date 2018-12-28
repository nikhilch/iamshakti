from __future__ import unicode_literals

from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, blank=True, null=True)
    postdate = models.DateField()
    cwarning = models.CharField(max_length=300, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    text = models.CharField(max_length=8000, blank=True, null=True)
    mediaurl = models.CharField(max_length=2000, blank=True, null=True)
    storyid = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'stories'
