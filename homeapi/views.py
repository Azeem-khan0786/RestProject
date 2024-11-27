from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Student
from .serializers import Student_serializer, UserSerializer
from django.contrib.auth import authenticate,login
from django.shortcuts import HttpResponse

@api_view(['GET','POST'])
def index(request):
    data=[{'name':'khan','email':'xya@zmq.in'}]

    # return HttpResponse('Hello gauys')
    return Response (data)

# @api_view(['GET'])
# def get_student(request):
#     students = Student.objects.all()
#     serializer = Student_serializer(students, many=True)
#     return Response({'status': 200, 'payload': serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data=request.data
#     serializer=Student_serializer(data=request.data)
#     if not  serializer.is_valid():
#         return Response({'status': 400, 'error': serializer.errors})
#     serializer.save()
#     return Response({'status': 201, 'payload': serializer.data})

        
 

@api_view(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        # Handle POST request logic here
        # For now, just return a success message
        return Response({'message': 'Resource created successfully',"status":"status.HTTP_201_CREATED"} )
    return Response({'message': 'Hello Rest Framework'})

# Class based view APIView()
class StudentView(APIView):
    def get(self,request):
        student=Student.objects.all()
        serializer=Student_serializer(student,many=True)
        return Response({"status":200,'payload':serializer.data})
    
    def post(self,request):
       data=request.data
       serializer=Student_serializer(data=request.data)
       if not serializer.is_valid():
           return Response({'status':403,'payload':serializer.errors})
       serializer.save()
       return Response({'status':200,'payload':serializer.data})
       
    def patch(self,request):
        student_id=Student.objects.get(id=request.data['id'])
        data=request.data
        serializer=Student_serializer(student_id,data=request.data,partial=True)
        if not serializer.is_valid():
            return Response({"status":403,'payload':serializer.errors})
        serializer.save()
        return Response({"status":200,'payload':serializer.data})
    
    def delete(self,request):
        try:
            id=request.GET.get('id')
            Student_obj=Student.objects.get(id=id)
            Student_obj.delete()
            
            return Response({"status":200,'payload':"Deleted Successfully"})
        except Exception as e:
            return Response({'status':403,'message':'Invalid id '})
    def delete(self,request,id):
        id=request.GET.get('id')
        Student_obj=Student.objects.get(id=id)
        Student_obj.delete()

class LoginView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            user_serializer=UserSerializer(request.user)
            return Response({"status":200,'payload':user_serializer.data})
        else:
            return Response({"status":403,'message':'User not authenticated'})
        
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return Response({"status":200,'user':request.user, 'payload':"Login Successfully"})
        else:
            return Response({"status":403,'payload':"Invalid Credentials"})
        