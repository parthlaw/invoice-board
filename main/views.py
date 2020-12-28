from django.shortcuts import render, redirect
# Create your views here.


def main(request):
    if request.user.is_authenticated:
        User = request.user
        print("HI tets")
        return render(request, 'nav/nav.html', {"User": User})
    else:
        return redirect('/login')


def test(request):
    return render(request, 'main/test.html')
