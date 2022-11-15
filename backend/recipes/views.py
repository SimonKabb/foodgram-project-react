from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .filters import IngredientNameFilter
from .models import Ingredient, Tag
from .serializers import IngredientSerializer, TagSerializer
from .permissions import IsOwnerOrAdminOrReadOnly

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    filterset_class = IngredientNameFilter
