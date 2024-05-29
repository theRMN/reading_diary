from django.urls import path, include
from rest_framework import routers

from .views import BookViewSet, NoteViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet, basename='BookViewSet')
router.register(r'notes', NoteViewSet, basename='NoteViewSet')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
