from django.conf import settings
from news.forms import CommentForm


def test_max_news_on_homepage(client, news_home_url, list_news):
    """Проверяет, что количество новостей на главной странице не 
    превышает NEWS_COUNT_ON_HOME_PAGE."""
    response = client.get(news_home_url)
    assert 'object_list' in response.context
    news_count = response.context['object_list'].count()
    assert news_count <= settings.NEWS_COUNT_ON_HOME_PAGE


def test_news_sorted_by_freshness(client, news_home_url, list_news):
    """Проверяет, что новости отсортированы от самой свежей к самой 
    старой."""
    response = client.get(news_home_url)
    assert 'object_list' in response.context
    all_dates = [
        news.date for news in response.context['object_list']
    ]
    assert all_dates == sorted(all_dates, reverse=True)


def test_comments_sorted_chronologically(
    client,
    news_detail_url,
    list_comments
):
    """Проверяет, что комментарии отсортированы в хронологическом 
    порядке: старые в начале, новые — в конце."""
    response = client.get(news_detail_url)
    all_dates = [
        comment.created
        for comment in response.context['news'].comment_set.all()
    ]
    assert all_dates == sorted(all_dates)


def test_anonymous_client_has_no_form(client, news_detail_url):
    """Проверяет, что анонимный клиент не видит форму для добавления 
    комментария на странице новости."""
    response = client.get(news_detail_url)
    assert 'form' not in response.context


def test_authorized_client_has_form(client_reader, news_detail_url):
    """Проверяет, что авторизованный клиент видит форму для 
    добавления комментария на странице новости."""
    response = client_reader.get(news_detail_url)
    context = response.context
    assert 'form' in context
    assert isinstance(context['form'], CommentForm)
