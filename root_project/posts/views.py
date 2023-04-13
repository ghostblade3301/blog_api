from django.http import HttpResponse


def index():
    html_content = '<html><head><title>Крутой блог</title></head><body>'
    html_content += '<h1>Главная страница / все последние посты блога</h1>'
    html_content += '</body></html>'
    return HttpResponse(html_content)


def post_detail(pk):
    return HttpResponse(f'Пост блога под номером: {pk}')


def group_posts(slug):
    return HttpResponse(f'Все посты группы: {slug}')
