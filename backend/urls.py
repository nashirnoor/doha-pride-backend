"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booking.views import BookingViewSet,BookingTransferViewSet,TransferBookingAuditViewSet,DashboardStatsView,BookingCurrencyStatsView
from app import views
from django.conf import settings
from django.conf.urls.static import static
from chatapp.views import ChatAPIView, UnreadMessagesView
from contact.views import ContactView,ContactMessageView
from booking.views import CategoryListView,TravelAgencyTransferBookingsViewSet,TravelAgencyTourBookingsViewSet,TourBookingAuditViewSet,get_agency_dashboard_stats,TransferBookingAuditViewSetDashboard,TourBookingAuditViewSetDashboard
from ToursAndActivities.views import ToursAndActivitiesDetailView,ToursListView,TopActivitiesListView,TourBookingView
from about.views import StatisticListCreateAPIView,ActivityListCreateAPIView,DescriptionDetailView
from driver.views import AuthViewSet,BannerViewSet,DriverFeedbackViewSet,DriverViewSet,DriverProfile
from home.views import BlogPostViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'bookings-tour', BookingViewSet)
router.register(r'bookings-transfer', BookingTransferViewSet,basename='booking-transfer')
router.register(r'drivers', DriverViewSet, basename='drivers')
router.register('auth', AuthViewSet, basename='auth')
router.register('banners', BannerViewSet)
router.register(r'blogs', BlogPostViewSet)
router.register('driver-feedback', DriverFeedbackViewSet)
router.register('transfer-audit', TransferBookingAuditViewSet,basename='transfer-audit')
router.register('transfer-audit-dashboard', TransferBookingAuditViewSetDashboard,basename='transfer-audit-dashboard')
router.register('tour-audit-dashboard', TourBookingAuditViewSetDashboard,basename='tour-audit-dashboard')
router.register('tour-audit', TourBookingAuditViewSet)
# router.register(r'contact-messages', ContactMessageViewSet, basename='contact-messages')
router.register('driver-profile',DriverProfile,basename='driver-profile')
router.register(r'travel-agency-transfer', TravelAgencyTransferBookingsViewSet, basename='travel-agency-transfer')
router.register(r'travel-agency-tour', TravelAgencyTourBookingsViewSet, basename='travel-agency-tour')




urlpatterns = [
    path('api/', include(router.urls)),
    path('chat/', ChatAPIView.as_view(), name='chat'),
    path('unread-messages/', UnreadMessagesView.as_view(), name='unread-messages'),
    path('contact-messages/', ContactMessageView.as_view(), name='contact-messages'),
    path('contact-messages/<int:pk>/', ContactMessageView.as_view(), name='contact-messages-detail'),
    # path('',include('chat.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('dashboard-stats/', DashboardStatsView.as_view(), name='booking-counts'),
    path('tour-currency-stats/', BookingCurrencyStatsView.as_view(), name='tour-currency-stats'),
    path('agency-dashboard-stats/', get_agency_dashboard_stats, name='booking-counts-agency'),
    path('transfer-meet-assist/', views.TransferMeetAssistList.as_view(), name='transfer-meet-assist-list'),
    path('contact/',  ContactView.as_view(), name='contact'),
    path('statistics/', StatisticListCreateAPIView.as_view(), name='statistic-list'),
    path('activities/', ActivityListCreateAPIView.as_view(), name='activity-list'),
    path('about-description/', DescriptionDetailView.as_view(), name='about-description'),
    path('tours/', ToursListView.as_view(), name='tours-list'),
    path('tours/<int:id>/', ToursAndActivitiesDetailView.as_view(), name='tour-detail'),
    path('top-activities/', TopActivitiesListView.as_view(), name='top-activities-list'),
    path('tour-booking/', TourBookingView.as_view(), name='tour-booking'),
    path('api/hotel-categories/', CategoryListView.as_view(), name='category-list'),
    path('api/banners-home/', views.HomeBannerListView.as_view(), name='banner-home'),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
