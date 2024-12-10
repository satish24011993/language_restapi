from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('languages',views.LanguageViewset, basename='language'),
# ]

router = DefaultRouter()

router.register(r'languages', views.LanguageViewset, basename='languages')
urlpatterns = router.urls
