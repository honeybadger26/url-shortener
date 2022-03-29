from django.shortcuts import render, redirect

from .models import URL

def _get_main_context(request) -> dict:
    return {
        'root_uri': request.build_absolute_uri()[:-1],
        'url_list': URL.objects.all()
    }

def index(request):
    return render(request, 'index.html', _get_main_context(request))

def create(request):
    if 'original_url' not in request.POST:
        return redirect('/')

    new_url = URL(original_url=request.POST['original_url'])
    error_msg = new_url.validate()

    if error_msg == '':
        new_url.save()
        return redirect('/')

    context = {
        'error': error_msg,
        **_get_main_context(request)
    }
    return render(request, 'index.html', context)

def goto(request, short_url):
    try:
        url = URL.objects.get(short_url=short_url)
        url.times_used += 1
        url.save()

        try:
            redir = redirect(url.original_url)
        except:
            return redirect('/')

        return redir
    except URL.DoesNotExist:
        pass