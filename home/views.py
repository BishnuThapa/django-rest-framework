from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


# @api_view(['POST', 'GET'])
@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)

    return Response({'status': 200, 'payload': serializer.data})


@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
    serializer.save()
    return Response({'status': 200, 'payload': serializer.data, 'message': 'Saved Successfully!'})


@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status': 200, 'message': 'Deleted Successfully!'})
    except Exception as e:
        return Response({'status': 403, 'message': 'invalid id'})
