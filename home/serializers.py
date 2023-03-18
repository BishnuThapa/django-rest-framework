from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # Validate if age is less than 18
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError(
                {'error': "age cannot be less than 18"})
        return data
