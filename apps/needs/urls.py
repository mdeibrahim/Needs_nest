from django.urls import path
from project import settings
from .views import AddNeedsAPIView, NeedsListAPIView, NeedsDetailAPIView, NeedsUpdateAPIView, NeedsDeleteAPIView
# from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('needs/', NeedsListAPIView.as_view(), name='needs-list'),
    path('add-needs/', AddNeedsAPIView.as_view(), name='add-needs'),
    path('needs-detail/<int:pk>/', NeedsDetailAPIView.as_view(), name='needs-detail'),
    path('needs-update/<int:pk>/', NeedsUpdateAPIView.as_view(), name='needs-update'),
    path('needs-delete/<int:pk>/', NeedsDeleteAPIView.as_view(), name='needs-delete'),
    # path('needs/<int:pk>/comments/', CommentsListAPIView.as_view(), name='comments-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)