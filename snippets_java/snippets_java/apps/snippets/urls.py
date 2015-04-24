from rest_framework import routers

from .views import SnippetViewSet


router = routers.SimpleRouter()
router.register(r'snippets', SnippetViewSet)

urlpatterns = router.urls