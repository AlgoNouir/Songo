


from django.shortcuts import render


def test(request, *args, **kwargs):
    return render(request, "new.html")