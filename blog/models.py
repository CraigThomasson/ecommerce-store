from django.db import models

class Blog(models.Model):
    """
    modle for blog page
    """

title = models.CharField(max_length=250, null=False, unique=True)
body = models.TextField()
added_on = models.DateTimeField(auto_now= True)

class Meta:
        ordering = ['-created_on']

def __str__(self):
    return self.title