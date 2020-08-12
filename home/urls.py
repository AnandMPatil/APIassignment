from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails , ArticleViewSet1, ArticleViewSet, MembersViewSet, MembersAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article1', ArticleViewSet1, basename='article1')
router.register('article', ArticleViewSet, basename='article')
router.register('members', MembersViewSet, basename='members')

urlpatterns = [
    path('', ArticleAPIView.as_view()),
    path('<int:pk>/', ArticleDetails.as_view()),
    path('members/', MembersAPIView.as_view()),
    path('viewset/', include(router.urls))
]
