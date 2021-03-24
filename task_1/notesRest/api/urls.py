from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet



router_v1 = DefaultRouter()
router_v1.register('notes', NoteViewSet)


urlpatterns = [
    path('v1/', include(router_v1.urls)),

]