from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Story(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, blank=True, null=True)
    postdate = models.DateField()
    cwarning = models.CharField(max_length=300, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=250)
    mediaurl = models.CharField(max_length=2000, blank=True, null=True)
    storyid = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

    def get_absolute_path(self):
        """
        Return the path for a given Story. For example, a story called "My Story" published on 1/2/2018 would have a URL of `stories/2018/1/2/my-story`.
        """
        return reverse('story_detail', args=[self.postdate.year, self.postdate.month, self.postdate.day, self.slug])

    class Meta:
        db_table = 'stories'
        verbose_name_plural = 'stories'
        ordering = ['-postdate']
