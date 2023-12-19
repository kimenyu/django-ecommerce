from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

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
    # permission_classes = (IsAuthenticated,)

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

    def get_queryset(self):
        """
        Custom queryset to filter products by name.

        Returns:
        - Queryset: Filtered queryset based on query parameters.
        """
        queryset = Product.objects.all()
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

    def perform_destroy(self, instance):
        """
        Perform the deletion of an existing product instance.

        Parameters:
        - `instance` (Product): The existing product instance to delete.

        Returns:
        - None
        """
        instance.delete()
