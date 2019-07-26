from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField
from dashboard.models import Rules
from dashboard.models import RulesCategory
from dashboard.models import FAQ
from dashboard.models import FAQCategory

class FAQCategorySerializer(ModelSerializer):
    class Meta:
        model = FAQCategory
        fields = ('sku', 'title', 'activate')
        read_only_fields = ('sku',)

class FAQSerializer(ModelSerializer):
    category = SlugRelatedField(queryset = FAQCategory.objects.all(), slug_field='title')

    class Meta:
        model = FAQ
        fields = ('title', 'description', 'activate', 'category')

class RulesCategorySerializer(ModelSerializer):
    class Meta:
        model = RulesCategory
        fields = ('sku', 'title', 'activate')
        read_only_fields = ('sku',)

class RulesSerializer(ModelSerializer):
    category = SlugRelatedField(queryset = RulesCategory.objects.all(), slug_field='title')

    class Meta:
        model = Rules
        fields = ('title', 'description', 'activate', 'category')
        depth = 1
