from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger
                                   )
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import (render,
                              get_object_or_404
                              )
from django.utils import timezone

from .forms import (CommentForm,
                    LikesForm
                    )
from .models import (Product,
                     ProductComments,
                     ProductLikes
                     )


def index(request):
    template_name = 'product/products_list.html'
    order_by = request.GET.get('order_by')
    products = Product.objects.all()
    if order_by == 'likes':
        products = products.annotate(l=Count('likes__text')).order_by('-l')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        prod = paginator.page(page)
    except PageNotAnInteger:
        prod = paginator.page(1)
    except EmptyPage:
        prod = paginator.page(paginator.num_pages)
    context = {
        'products': prod,
        'order_by': order_by

    }
    return render(request, template_name, context)


def product_detail(request, slug):
    template_name = 'product/product_detail.html'
    day_before = timezone.now() - timezone.timedelta(days=1)
    product = get_object_or_404(Product, slug=slug)
    comments = ProductComments.objects.filter(product__slug=slug,
                                              created_at__gte=day_before
                                              )
    context = {
        'comments': comments,
        'product': product,
    }
    response = render(request, template_name, context)
    return response


def likes(request):
    form = LikesForm(request.POST or None)
    print 'request.user.profile', request.user.profile.is_blocked == False
    if (request.POST and form.is_valid() and
            request.is_ajax() and request.user.profile.is_blocked == False
        ):
        product = form.cleaned_data['product']
        user = request.user.profile.id
        user_likes_in_product = ProductLikes.objects.filter(user=user,
                                                            product_id=product
                                                            )
        if user_likes_in_product.count() == 0:
            form = form.save(commit=False)
            form.user_id = user
            form.save()
            status = 'False'
        else:
            status = 'True'
        context = {
            'status': status
        }
    else:
        print 'blocked user'
        context = {
            'status': 'blocked'
        }
    return JsonResponse(context)


def add_comment(request):
    form = CommentForm(request.POST or None)
    status = 'False'
    if (request.POST and form.is_valid() and
            request.is_ajax() and request.user.profile.is_blocked == False):
        form = form.save(commit=False)

        form.user_id = request.user.profile.id
        form.save()
        text = form.text
        context = {
            'text': text,
            'status': 'success'
        }
        return JsonResponse(context)
    elif (request.POST and form.is_valid() and
              request.is_ajax() and request.user.profile.is_blocked == True):
        print 'blocked'
        return JsonResponse({'status': 'blocked'})

    else:
        return JsonResponse({'status': status})
