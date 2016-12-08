from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('company', 'title', 'rating', 'submission_date', 'reviewer',)
