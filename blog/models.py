from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(config_name='awesome_ckeditor')
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
