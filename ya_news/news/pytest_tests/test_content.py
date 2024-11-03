from django.conf import settings

from news.forms import CommentForm


def test_max_news_on_homepage(client, news_home_url, list_news):
    """Проверка, что на главной странице не более X новостей."""
    response = client.get(news_home_url)
    assert 'object_list' in response.context
    assert response.context['object_list'].count(
    ) == settings.NEWS_COUNT_ON_HOME_PAGE


def test_news_sorted_by_freshness(client, news_home_url, list_news):
    """
    Проверка сортировки новостей от самой свежей к самой старой.
    Свежие новости в начале списка.
    """
    response = client.get(news_home_url)
    assert 'object_list' in response.context
    all_dates = [news.date for news in response.context['object_list']]
    assert all_dates == sorted(all_dates, reverse=True)


def test_comments_sorted_chronologically(
    client, news_detail_url, list_comments
):
    """
    Проверка сортировки комментариев в хронологическом порядке:
    старые в начале списка, новые — в конце.
    """
    all_dates = [
        comment.created
        for comment in client.get(news_detail_url)
        .context['news']
        .comment_set.all()
    ]
    assert all_dates == sorted(all_dates)


def test_anonymous_client_has_no_form(client, news_detail_url):
    """Проверка, что анонимный клиент не видит форму комментариев."""
    assert 'form' not in client.get(news_detail_url).context


def test_authorized_client_has_form(client_reader, news_detail_url):
    """Проверка, что авторизованный клиент видит форму комментариев."""
    context = client_reader.get(news_detail_url).context
    assert 'form' in context
    assert isinstance(context['form'], CommentForm)
