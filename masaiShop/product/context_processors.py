from .models import Category

def show_categories(request):
    return {'categories': Category.objects.all()}