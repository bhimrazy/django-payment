from django.http import HttpResponse

def index(request): 
    """Main index route of website"""
    return HttpResponse("Welcome to Payment Module App.")