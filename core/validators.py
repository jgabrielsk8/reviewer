from django.core.exceptions import ValidationError


def validate_ratings(value):
    if value < 1 or value > 5:
        raise ValidationError('Ratings must be in range from 1 through 5.')
