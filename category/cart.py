

from .models import ProductModel

class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('cart')
        if cart is None:
            cart = self.session['cart']={}
        self.cart = cart

        self.total_price=0
    def Add(self,product,number):
        product_id = str(product.id)
        if product_id not in self.cart.keys():
            self.cart[product_id]={'number':0,'price':str(product.price)}
        self.cart[product_id]['number'] = number
        self.session.modified = True
        return self.get_total()
    def Remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart.keys():
            del self.cart[product_id]
        self.session.modified = True


    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductModel.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
           cart[str(product.id)]['product'] = product
                 
        for item in cart.values():
            item['total'] =str( int(item['number']) * int(item['price']))
            self.total_price += int(item['total'])
            item['total_price'] =str( self.total_price)
            yield item
    def get_total(self):
        return self.total_price
    def get_total2(self,product):
        product_id = str(product.id)
        return (self.cart[product_id]['total'])


