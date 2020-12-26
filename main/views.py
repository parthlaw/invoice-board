from django.shortcuts import render, redirect
# Create your views here.


def main(request):
    if request.user.is_authenticated:
        User = request.user
        return render(request, 'nav/nav.html', {"User": User})
    else:
        return redirect('/login')
