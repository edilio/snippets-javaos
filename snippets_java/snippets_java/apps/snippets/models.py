from django.db import models
from django.conf import settings

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
LANGUAGE_CHOICES = [('java', 'Java')]
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='java', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ('created_on',)

    def __unicode__(self):
        return self.title
