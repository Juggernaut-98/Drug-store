from products.models import category


def categories(request):
    categories=[]
    for key in category.objects.all():
        categories.append(key)
    return {'categories': categories}
