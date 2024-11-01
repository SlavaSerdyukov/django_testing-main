import pytest

from news.models import Article, Comment


@pytest.mark.django_db
def test_article_creation():
    """Проверяет создание статьи."""
    article = Article.objects.create(
        title="Тестовая статья",
        content="Содержимое тестовой статьи."
    )
    assert article.title == "Тестовая статья"
    assert article.content == "Содержимое тестовой статьи."


@pytest.mark.django_db
def test_article_str_method():
    """Проверяет метод __str__ статьи."""
    article = Article.objects.create(
        title="Тестовая статья",
        content="Содержимое тестовой статьи."
    )
    assert str(article) == "Тестовая статья"


@pytest.mark.django_db
def test_comment_creation(article):
    """Проверяет создание комментария к статье."""
    comment = Comment.objects.create(
        article=article,
        text="Это тестовый комментарий."
    )
    assert comment.article == article
    assert comment.text == "Это тестовый комментарий."


@pytest.mark.django_db
def test_comment_str_method(comment):
    """Проверяет метод __str__ комментария."""
    assert str(comment) == comment.text[:20]
