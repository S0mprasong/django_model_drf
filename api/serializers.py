from rest_framework import serializers
from .models import Reporter, Article, ArticleDetail


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetail
        fields = ('pk','detial',)


class ArticleSerializer(serializers.ModelSerializer):
    article_detail = ArticleDetailSerializer(many=False, read_only=False)
    # article_detail = serializers.StringRelatedField(many=False)
    class Meta:
        model = Article
        fields = ('pk','headline', 'pub_date', 'article_detail')


class ReporterSerializer(serializers.ModelSerializer):
    # article = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    total_article = serializers.SerializerMethodField('calculate_total_article')
    article = ArticleSerializer(many=True, read_only=False)

    def calculate_total_article(self,obj):
        reporter = Reporter.objects.get(pk=1)
        return reporter.article.count()

    class Meta:
        model = Reporter
        fields = ('pk','first_name', 'email', 'article','total_article')