from django.db import models


class News_letter(models.Model):
    """
    modle for news letters
    """
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
