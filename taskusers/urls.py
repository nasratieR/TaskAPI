from unicodedata import name
from django.urls import include, path
from rest_framework import routers
from taskusers.users import views as users_views
from taskusers.tasks import views as tasks_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="TASK API",
        default_version="v1"
    ),
    public=True,
    #permission_classes=(permissions.AllowAny)
)

router = routers.DefaultRouter()
router.register(r'users', users_views.UserViewSet)
router.register(r'groups', users_views.GroupViewSet)
router.register(r'tasks', tasks_views.TasksViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]