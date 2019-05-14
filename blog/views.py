from django.shortcuts import render

posts = [
    {
        'author': 'Sunil',
        'title': 'Blog post 1',
        'content': 'First post',
        'date_posted': 'May 10'

    },
    {
        'author': 'Sekar',
        'title': 'Blog post 2',
        'content': 'Second post',
        'date_posted': 'May 11'

    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})