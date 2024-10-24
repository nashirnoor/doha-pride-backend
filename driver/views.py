from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework import status
from .models import Banner,DriverFeedback
from booking.models import TransferBooking
from booking.serializers import DriverTransferBookingSerializer
from .serializers import BannerSerializer,DriverFeedbackSerializer
import logging
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


logger = logging.getLogger(__name__)


User = get_user_model()

@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
@method_decorator(csrf_exempt, name='dispatch')
class AuthViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'user': UserSerializer(user).data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def user(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def driver_bookings(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if request.user.user_type != 'driver':
            return Response({'error': 'Only drivers can access this endpoint'}, status=status.HTTP_403_FORBIDDEN)

        today = timezone.now().date()
        try:
            bookings = TransferBooking.objects.filter(
                driver=request.user,
                date=today
            )
            serializer = DriverTransferBookingSerializer(bookings, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': 'An error occurred while fetching bookings'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=False, methods=['get'])
    def completed_bookings(self, request):
        if not request.user.is_authenticated:
            return Response(
                {'error': 'Authentication required'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        if request.user.user_type != 'driver':
            return Response(
                {'error': 'Only drivers can access this endpoint'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            bookings = TransferBooking.objects.filter(
                driver=request.user,
                status='done'  # Filter for completed bookings
            ).order_by('-date')  # Most recent first
            
            serializer = DriverTransferBookingSerializer(bookings, many=True)
            return Response(serializer.data)
            
        except Exception as e:
            return Response(
                {'error': 'An error occurred while fetching completed bookings'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class DriverFeedbackViewSet(viewsets.ModelViewSet):
    queryset = DriverFeedback.objects.all()
    serializer_class = DriverFeedbackSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(user_type='driver')
