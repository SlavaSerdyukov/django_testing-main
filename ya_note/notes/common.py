from http import HTTPStatus


WARNING = "Это предупреждение"
NOTES_ADD = "/notes/add/"
NOTES_EDIT = "/notes/edit/"
NOTE_SLUG = "slug-note"


def slugify(title):
    """Превращает строку в slug, пригодный для URL."""
    return title.lower().replace(' ', '-')


class BaseTestCase:
    """Базовый класс для тестов."""
    pass
