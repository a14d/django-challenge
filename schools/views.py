from rest_framework import viewsets, filters
from .serializers import SchoolSerializer, StudentSerializer
from .models import School, Student

# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed and edited
    Note: The school will be added based on the URL not the browsable API
    """
    queryset         = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends  = [filters.SearchFilter, filters.OrderingFilter]
    search_fields    = ['first_name', 'last_name']
    ordering_fields  = ['first_name', 'last_name']

    def get_queryset(self):
        school = self.kwargs.get('school_pk', None)

        if school:
            return Student.objects.filter(school=self.kwargs['school_pk'])
        
        return self.queryset
    
    def perform_create(self, serializer):
        school = School.objects.get(pk=self.kwargs['school_pk'])
        serializer.save(school=school)
    