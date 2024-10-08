from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.api.v1.bookmark.api import BookmarkViewSet
# from apps.api.v1.home.api import HomeViewSet
# from apps.api.v1.user.api import UserViewSet
# from apps.api.v1.word.api import WordViewSet
# from apps.api.v1.vocabulary.api import VocabularyViewSet
# from apps.api.v1.training.api import TrainingViewSet
# from apps.api.v1.jwt.api import JWTViewSet
# from apps.api.v1.search.api import SearchViewSet

router = SimpleRouter()
router.register(r'bookmarks', BookmarkViewSet, basename='bookmark')
# router.register(r'home', HomeViewSet, basename='home')
# router.register(r'users', UserViewSet, basename='user')
# router.register(r'words', WordViewSet, basename='word')
# router.register(r'vocabulary', VocabularyViewSet, basename='vocabulary')
# router.register(r'training', TrainingViewSet, basename='training')
# router.register(r'jwt', JWTViewSet, basename='jwt')


urlpatterns = [
    path('', include(router.urls)),
    # home
    path('home/', include('apps.api.v1.home.urls')),
    path('books/', include('apps.api.v1.book.urls')),
    path('users/', include('apps.api.v1.user.urls')),
    path('words/', include('apps.api.v1.word.urls')),
    path('vocabulary/', include('apps.api.v1.vocabulary.urls')),
    path('training/', include('apps.api.v1.training.urls')),
    path('jwt/', include('apps.api.v1.jwt.urls')),
    path('stats/', include('apps.api.v1.stats.urls')),
    
    
    path('dev/', include('apps.api.v1.dev.urls'))
] 