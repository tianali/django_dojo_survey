from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inputs(request):
    if request.method == 'POST':
        request.session['fname'] = request.POST['fname']
        request.session['gender'] = request.POST['gender']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
    return redirect('/result')

def result(request):
    context = {
        'fname': request.session['fname'],
        'gender': request.session['gender'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comments': request.session['comments'],
    }
    return render(request, 'result.html', context)