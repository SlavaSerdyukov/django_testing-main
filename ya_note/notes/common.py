WARNING = "Это предупреждение"
NOTES_ADD = "/notes/add/"
NOTES_EDIT = "/notes/edit/"
NOTES_LIST = "/notes/list/"
NOTE_SLUG = "slug-note"


def slugify(title):
    return title.lower().replace(' ', '-')


class BaseTestCase:
    pass
