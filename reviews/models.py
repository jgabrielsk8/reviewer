from django.db import models
from django.contrib.auth.models import User

from core.models import Company
from core.validators import validate_ratings


class Review(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=64)
    rating = models.IntegerField(validators=[validate_ratings])
    summary = models.CharField(max_length=10000)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    reviewer = models.ForeignKey(User)
