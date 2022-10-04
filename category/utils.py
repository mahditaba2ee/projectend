from urllib import request


def shopping_cart(request):
    buys=[]
    for c in list(request.session['cart'].keys()):
                buys.append(int(c))
    return buys

