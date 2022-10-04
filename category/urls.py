from operator import ne
from django.urls import path
from .views import *
from .send_email import SendEmailView
app_name='category'

urlpatterns=[
    path('',CategoryView.as_view(),name='category'),

    # path('/<str:strproduct>/',CategoryView.as_view(),name='category'),
    # path('cat/<str:strproduct>',SearchView2.as_view(),name='searc'),
    
    path('add',AddProductView.as_view(),name='addproduct'),
    path('cart/',CartView.as_view(),name='cart'),
    path('card/add/',CartAddView.as_view(),name='cartadd'),
    path('card/remove/',CartRemoveView.as_view(),name='cartremove'),

    path('order/',OrderView.as_view(),name='order'),
    path('sendorder/',SendOrderView.as_view(),name='sendorder'),
    path('sendorder/submit/',SubmitOrderView.as_view(),name='submitorder'),
    path('oldorders/',OldOrderView.as_view(),name='oldorders'),
    path('sendorderuser/',SendOrderUserView.as_view(),name='sendorderuser'),
    path('sendorder/back/',BackOrderView.as_view(),name='backorder'),
    path('commentadd/',CommentAddView.as_view(),name='comment'),
    path('search/<str:strproduct>',SearchView.as_view(),name='search'),
    path('search/category/<slug:category_slug>',SearchCategoryView.as_view(),name='searchcategory'),

    # path('<slug:slug>/<slug:brand_slug>',SearchView.as_view(),name='search_type'),
    path('like/',LikeView.as_view(),name='like'),
    path('send/email/user/',SendEmailView.as_view(),name='sendemail'),

    path('cat/choise/',ChoiseView.as_view(),name='choise'),
    path('details/product/<str:cat_slug>/<str:brand_slug>/<str:product_slug>',ProductDetailsView.as_view(),name='datails'),
    path('addstar/',StarAddView.as_view(),name="addstar"),
    path('sharepost/',SharePostView.as_view(),name="addstar"),
    path('addbrand',AddBrandView.as_view(),name='addbrand'),
    path('addcategory',AddCategoryView.as_view(),name='addcategory'),
    path('addtype',AddTypeView.as_view(),name='addtype'),

    ]