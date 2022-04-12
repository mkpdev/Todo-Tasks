from rest_framework.routers import DefaultRouter
from .views import Tasks

router = DefaultRouter()
router.register(r'tasks', Tasks)
urlpatterns = router.urls