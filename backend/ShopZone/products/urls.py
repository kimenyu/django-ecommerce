from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    #create products urls
    path('create/', ProductCreateView.as_view(), name='create-product'),
    
    #list products urls
    path('list/', ProductListView.as_view(), name='list-product'),
    
    #detail of products
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail-product'),
    
    #update products url
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update-product'),
    
    #delete products url
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)