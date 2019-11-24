from rest_framework import serializers

from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model  = School
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Student
        fields = '__all__'

    def validate(self, data):
        school = data['school']
        student_count = school.student_set.count()

        if student_count >= school.max_students:
            raise serializers.ValidationError("The school is full right now.")

        return data