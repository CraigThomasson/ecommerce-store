from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import NewsLetterForm


def index(request):
    """
    veiw from home page
    """
    return render(request, 'home/index.html')


def about(request):
    """
    veiw from home page
    """
    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added to mail list')
            return redirect(reverse('about',))
        else:
            messages.error(
                request, 'you where not added to the mail list. \
                     Please check the form is valid.'
            )
    else:
        form = NewsLetterForm()
    
    template = 'home/about.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
