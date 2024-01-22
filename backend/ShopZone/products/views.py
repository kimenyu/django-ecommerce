from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Product, Category, Cart, CartItem, ContactInfo, Profile, Order
from .serializers import ProductSerializer, CategorySerializer, CartSerializer, CartItemSerializer, ContactInfoSerializer, ProfileSerializer, OrderSerializer
from rest_framework import permissions 
from django_daraja.mpesa.core import MpesaClient
from .pagination import SmallSetPagination
from .permissions import IsAdminUserorReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import permissions
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

# Create your views here.
def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0793058968'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://api.darajambili.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("STK Push in Django👋")


class ProductCreateView(CreateAPIView):
    """
    CreateAPIView for creating a new product.

    HTTP Methods:
    - POST: Create a new product.

    Request Data:
    - JSON object containing product details.

    Response:
    - 201 Created: Product created successfully.
    - 400 Bad Request: Invalid data provided.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserorReadOnly]

    def perform_create(self, serializer):
        """
        Perform the creation of a new product instance.

        Parameters:
        - `serializer` (ProductSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class ProductListView(ListAPIView):
    """
    ListAPIView for retrieving a list of products.

    HTTP Methods:
    - GET: Retrieve a list of products.

    Query Parameters:
    - `name` (optional): Filter products by name.

    Response:
    - 200 OK: Returns a list of products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = SmallSetPagination
    permission_classes = [permissions.AllowAny]
    


    def get_queryset(self):
        """
        Custom queryset to filter products by name.

        Returns:
        - Queryset: Filtered queryset based on query parameters.
        """
        queryset = Product.objects.all().order_by("-id")
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class ProductDetailView(RetrieveAPIView):
    """
    RetrieveAPIView for retrieving details of a specific product.

    HTTP Methods:
    - GET: Retrieve details of a specific product.

    Response:
    - 200 OK: Returns details of the requested product.
    - 404 Not Found: Product not found.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductUpdateView(UpdateAPIView):
    """
    UpdateAPIView for updating details of a specific product.

    HTTP Methods:
    - PUT/PATCH: Update details of a specific product.

    Request Data:
    - JSON object containing updated product details.

    Response:
    - 200 OK: Product updated successfully.
    - 400 Bad Request: Invalid data provided.
    - 404 Not Found: Product not found.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserorReadOnly]

    def perform_update(self, serializer):
        """
        Perform the update of an existing product instance.

        Parameters:
        - `serializer` (ProductSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class ProductDeleteView(DestroyAPIView):
    """
    DestroyAPIView for deleting a specific product.

    HTTP Methods:
    - DELETE: Delete a specific product.

    Response:
    - 204 No Content: Product deleted successfully.
    - 404 Not Found: Product not found.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserorReadOnly]

    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing product instance.

        Parameters:
        - `instance` (Product): The existing product instance to delete.

        Returns:
        - None
        """
        instance.delete()

class CategoryCreateView(CreateAPIView):
    """
    CreateAPIView for creating a new category.

    HTTP Methods:
    - POST: Create a new category.

    Request Data:
    - JSON object containing category details.

    Response:
    - 201 Created: Category created successfully.
    - 400 Bad Request: Invalid data provided.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserorReadOnly]

    def perform_create(self, serializer):
        """
        Perform the creation of a new category instance.

        Parameters:
        - `serializer` (CategorySerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class CategoryListView(ListAPIView):
    """
    ListAPIView for retrieving a list of categories.

    HTTP Methods:
    - GET: Retrieve a list of categories.

    Response:
    - 200 OK: Returns a list of categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserorReadOnly]

class CategoryDetailView(RetrieveAPIView):
    """
    RetrieveAPIView for retrieving details of a specific category.

    HTTP Methods:
    - GET: Retrieve details of a specific category.

    Response:
    - 200 OK: Returns details of the requested category.
    - 404 Not Found: Category not found.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserorReadOnly]

class CategoryUpdateView(UpdateAPIView):
    """
    UpdateAPIView for updating details of a specific category.

    HTTP Methods:
    - PUT/PATCH: Update details of a specific category.

    Request Data:
    - JSON object containing updated category details.

    Response:
    - 200 OK: Category updated successfully.
    - 400 Bad Request: Invalid data provided.
    - 404 Not Found: Category not found.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserorReadOnly]

    def perform_update(self, serializer):
        """
        Perform the update of an existing category instance.

        Parameters:
        - `serializer` (CategorySerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class CategoryDeleteView(DestroyAPIView):
    """
    DestroyAPIView for deleting a specific category.

    HTTP Methods:
    - DELETE: Delete a specific category.

    Response:
    - 204 No Content: Category deleted successfully.
    - 404 Not Found: Category not found.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserorReadOnly]

    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing category instance.

        Parameters:
        - `instance` (Category): The existing category instance to delete.

        Returns:
        - None
        """
        instance.delete()

class CartCreateView(CreateAPIView):
    """
    CreateAPIView for creating a new cart.

    HTTP Methods:
    - POST: Create a new cart.

    Request Data:
    - JSON object containing cart details.

    Response:
    - 201 Created: Cart created successfully.
    - 400 Bad Request: Invalid data provided.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Perform the creation of a new cart instance.

        Parameters:
        - `serializer` (CartSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class CartListView(ListAPIView):
    """
    ListAPIView for retrieving a list of carts.

    HTTP Methods:
    - GET: Retrieve a list of carts.

    Response:
    - 200 OK: Returns a list of carts.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

class CartDetailView(RetrieveAPIView):
    """
    RetrieveAPIView for retrieving details of a specific cart.

    HTTP Methods:
    - GET: Retrieve details of a specific cart.

    Response:
    - 200 OK: Returns details of the requested cart.
    - 404 Not Found: Cart not found.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

class CartUpdateView(UpdateAPIView):
    """
    UpdateAPIView for updating details of a specific cart.

    HTTP Methods:
    - PUT/PATCH: Update details of a specific cart.

    Request Data:
    - JSON object containing updated cart details.

    Response:
    - 200 OK: Cart updated successfully.
    - 400 Bad Request: Invalid data provided.
    - 404 Not Found: Cart not found.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Perform the update of an existing cart instance.

        Parameters:
        - `serializer` (CartSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class CartDeleteView(DestroyAPIView):
    """
    DestroyAPIView for deleting a specific cart.

    HTTP Methods:
    - DELETE: Delete a specific cart.

    Response:
    - 204 No Content: Cart deleted successfully.
    - 404 Not Found: Cart not found.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing cart instance.

        Parameters:
        - `instance` (Cart): The existing cart instance to delete.

        Returns:
        - None
        """
        instance.delete()

class CartItemCreateView(CreateAPIView):
    """
    CreateAPIView for creating a new cart item.

    HTTP Methods:
    - POST: Create a new cart item.

    Request Data:
    - JSON object containing cart item details.

    Response:
    - 201 Created: Cart item created successfully.
    - 400 Bad Request: Invalid data provided.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Perform the creation of a new cart item instance.

        Parameters:
        - `serializer` (CartItemSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class CartItemListView(ListAPIView):
    """
    ListAPIView for retrieving a list of cart items.

    HTTP Methods:
    - GET: Retrieve a list of cart items.

    Response:
    - 200 OK: Returns a list of cart items.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class CartItemDetailView(RetrieveAPIView):
    """
    RetrieveAPIView for retrieving details of a specific cart item.

    HTTP Methods:
    - GET: Retrieve details of a specific cart item.

    Response:
    - 200 OK: Returns details of the requested cart item.
    - 404 Not Found: Cart item not found.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartItemUpdateView(UpdateAPIView):
    """
    UpdateAPIView for updating details of a specific cart item.

    HTTP Methods:
    - PUT/PATCH: Update details of a specific cart item.

    Request Data:
    - JSON object containing updated cart item details.

    Response:
    - 200 OK: Cart item updated successfully.
    - 400 Bad Request: Invalid data provided.
    - 404 Not Found: Cart item not found.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_update(self, serializer):
        """
        Perform the update of an existing cart item instance.

        Parameters:
        - `serializer` (CartItemSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class CartItemDeleteView(DestroyAPIView):
    """
    DestroyAPIView for deleting a specific cart item.

    HTTP Methods:
    - DELETE: Delete a specific cart item.

    Response:
    - 204 No Content: Cart item deleted successfully.
    - 404 Not Found: Cart item not found.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing cart item instance.

        Parameters:
        - `instance` (CartItem): The existing cart item instance to delete.

        Returns:
        - None
        """
        instance.delete()

class ContactInfoCreateView(CreateAPIView):
    """
    CreateAPIView for creating a new contact info.

    HTTP Methods:
    - POST: Create a new contact info.

    Request Data:
    - JSON object containing contact info details.

    Response:
    - 201 Created: Contact info created successfully.
    - 400 Bad Request: Invalid data provided.
    """
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        """
        Perform the creation of a new contact info instance.

        Parameters:
        - `serializer` (ContactInfoSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class ContactInfoListView(ListAPIView):
    """
    ListAPIView for retrieving a list of contact infos.

    HTTP Methods:
    - GET: Retrieve a list of contact infos.

    Response:
    - 200 OK: Returns a list of contact infos.
    """
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactInfoDetailView(RetrieveAPIView):
    """
    RetrieveAPIView for retrieving details of a specific contact info.

    HTTP Methods:
    - GET: Retrieve details of a specific contact info.

    Response:
    - 200 OK: Returns details of the requested contact info.
    - 404 Not Found: Contact info not found.
    """
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactInfoUpdateView(UpdateAPIView):
    """
    UpdateAPIView for updating details of a specific contact info.

    HTTP Methods:
    - PUT/PATCH: Update details of a specific contact info.

    Request Data:
    - JSON object containing updated contact info details.

    Response:
    - 200 OK: Contact info updated successfully.
    - 400 Bad Request: Invalid data provided.
    - 404 Not Found: Contact info not found.
    """
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_update(self, serializer):
        """
        Perform the update of an existing contact info instance.

        Parameters:
        - `serializer` (ContactInfoSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class ContactInfoDeleteView(DestroyAPIView):
    """
    DestroyAPIView for deleting a specific contact info.

    HTTP Methods:
    - DELETE: Delete a specific contact info.

    Response:
    - 204 No Content: Contact info deleted successfully.
    - 404 Not Found: Contact info not found.
    """
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing contact info instance.

        Parameters:
        - `instance` (ContactInfo): The existing contact info instance to delete.

        Returns:
        - None
        """
        instance.delete()
        
class ProfileCreateView(CreateAPIView):
    """
    CreateAPIView for creating a new profile.

    HTTP Methods:
    - POST: Create a new profile.

    Request Data:
    - JSON object containing profile details.

    Response:
    - 201 Created: Profile created successfully.
    - 400 Bad Request: Invalid data provided.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        """
        Perform the creation of a new profile instance.

        Parameters:
        - `serializer` (ProfileSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class ProfileListView(ListAPIView):
    """
    ListAPIView for retrieving a list of profiles.

    HTTP Methods:
    - GET: Retrieve a list of profiles.

    Response:
    - 200 OK: Returns a list of profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileDetailView(RetrieveAPIView):
    """
    RetrieveAPIView for retrieving details of a specific profile.

    HTTP Methods:
    - GET: Retrieve details of a specific profile.

    Response:
    - 200 OK: Returns details of the requested profile.
    - 404 Not Found: Profile not found.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class ProfileUpdateView(UpdateAPIView):
    """
    UpdateAPIView for updating details of a specific profile.

    HTTP Methods:
    - PUT/PATCH: Update details of a specific profile.

    Request Data:
    - JSON object containing updated profile details.

    Response:
    - 200 OK: Profile updated successfully.
    - 400 Bad Request: Invalid data provided.
    - 404 Not Found: Profile not found.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_update(self, serializer):
        """
        Perform the update of an existing profile instance.

        Parameters:
        - `serializer` (ProfileSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class ProfileDeleteView(DestroyAPIView):
    """
    DestroyAPIView for deleting a specific profile.

    HTTP Methods:
    - DELETE: Delete a specific profile.

    Response:
    - 204 No Content: Profile deleted successfully.
    - 404 Not Found: Profile not found.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing profile instance.

        Parameters:
        - `instance` (Profile): The existing profile instance to delete.

        Returns:
        - None
        """
        instance.delete()

class OrderCreateView(CreateAPIView):
    """
    CreateAPIView for creating a new order.

    HTTP Methods:
    - POST: Create a new order.

    Request Data:
    - JSON object containing order details.

    Response:
    - 201 Created: Order created successfully.
    - 400 Bad Request: Invalid data provided.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        """
        Perform the creation of a new order instance.

        Parameters:
        - `serializer` (OrderSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class OrderListView(ListAPIView):
    """
    ListAPIView for retrieving a list of orders.

    HTTP Methods:
    - GET: Retrieve a list of orders.

    Response:
    - 200 OK: Returns a list of orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderDetailView(RetrieveAPIView):
    """
    RetrieveAPIView for retrieving details of a specific order.

    HTTP Methods:
    - GET: Retrieve details of a specific order.

    Response:
    - 200 OK: Returns details of the requested order.
    - 404 Not Found: Order not found.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderUpdateView(UpdateAPIView):
    """
    UpdateAPIView for updating details of a specific order.

    HTTP Methods:
    - PUT/PATCH: Update details of a specific order.

    Request Data:
    - JSON object containing updated order details.

    Response:
    - 200 OK: Order updated successfully.
    - 400 Bad Request: Invalid data provided.
    - 404 Not Found: Order not found.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_update(self, serializer):
        """
        Perform the update of an existing order instance.

        Parameters:
        - `serializer` (OrderSerializer): The serializer instance.

        Returns:
        - None
        """
        serializer.save()

class OrderDeleteView(DestroyAPIView):
    """
    DestroyAPIView for deleting a specific order.

    HTTP Methods:
    - DELETE: Delete a specific order.

    Response:
    - 204 No Content: Order deleted successfully.
    - 404 Not Found: Order not found.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing order instance.

        Parameters:
        - `instance` (Order): The existing order instance to delete.

        Returns:
        - None
        """
        instance.delete()