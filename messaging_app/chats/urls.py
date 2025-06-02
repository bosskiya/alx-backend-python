from rest_framework_nested import routers
from .views import MessageViewSet, ConversationViewSet

router = routers.DefaultRouter()

#CHATS
router.register(r'conversations', ConversationViewSet, basename='conversations')

nested_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'message', MessageViewSet, basename='conversation-message')

urlpatterns = router.urls + nested_router.urls