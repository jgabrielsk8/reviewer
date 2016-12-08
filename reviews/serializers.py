from rest_framework import serializers
from core.helpers import get_client_ip
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(source='reviewer.username', read_only=True)
    company_name = serializers.PrimaryKeyRelatedField(source='company.name', read_only=True)

    class Meta:
        model = Review
        fields = ('company', 'company_name', 'title', 'rating', 'summary', 'ip_address', 'submission_date', 'reviewer')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data.update(reviewer=request.user,
                              ip_address=get_client_ip(request))
        return Review.objects.create(**validated_data)
