from django.shortcuts import render


def bag_view(request):
    """
    veiw from bag page
    """
    return render(request, 'bag/bag.html')
