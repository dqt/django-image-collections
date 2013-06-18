from django.db import models
from django.db.models import permalink

import os
from PIL import Image as PImage
from teensite.settings import MEDIA_ROOT

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(blank=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('myapp.Category')
    images = models.ManyToManyField('myapp.Image')

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('teensite.myapp.views.view_post', None, {'slug': self.slug})

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('teensite.myapp.views.view_category', None, {'slug': self.slug})

class Image(models.Model):

    def content_file_name(instance, filename):
        return os.path.join(MEDIA_ROOT, filename)

    title = models.CharField(max_length=60, blank=True, null=True)
    number = models.IntegerField()
    image = models.FileField(upload_to=content_file_name)
    body = models.TextField(blank=True)
    citation = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size
        super(Image, self).save(*args, ** kwargs)

    def __unicode__(self):
        return self.image.name

    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)

    def get_pic(self):
        return 'http://www.teensdigest.com/media/%s' % os.path.basename(self.image.name)