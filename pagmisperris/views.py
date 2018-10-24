from django.shortcuts import render

# Create your views here.
#def base(request):
    #return render(request, 'pagmisperris/base.html', {})

def post_list(request):
    return render(request, 'pagmisperris/post_list.html', {})