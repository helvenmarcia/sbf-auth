from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    """
    TODO:
    - Ambil "username" and "password" dari request.data
    - Validate: not empty, password length >= X
    - Check if username already exists -> return 400 | Hint: Pakai User.object.filter(username=username).exist() sebagai condition
    - Create user pakai User.object.create_user()
    - Return 201 with: { "message": "registered"}
    """
    return Response({"detail": "Not implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)

@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    """
    TODO:
    - Ambil username/password dari request.data
    - Cek kredensial user | Hint: Pakai authenticate(...)
    - If fail -> return invalid credentials 400
    - Else return { "token": <token> }
    """
    return Response({"detail": "Not implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def secret(request):
    """
    TODO:
    Buat function bebas, sekreatif atau sekocak mungkin
    Examples:
    - Return random number
    - Return custom message
    - Return a JSON list of your favorite movies
    - Return https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ
    - Anything
    """
    return Response({"detail": "Not implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)