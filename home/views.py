from django.shortcuts import render


def index(request):
    """
    veiw from home page
    """
    return render(request, 'home/index.html')

def about(request):
    """
    veiw from home page
    """
    return render(request, 'home/about.html')
