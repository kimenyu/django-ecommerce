from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.

    Fields:
    - `id`: The unique identifier for the category.
    - `name`: The name of the category.
    """
    class Meta:
        model = Category
        fields = ['id', 'name']
       
    def create(self, validated_data):
        """
        Create a new category instance.

        Parameters:
        - `validated_data` (dict): Validated data for creating the category.

        Returns:
        - `Category`: The created category instance.
        """
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing category instance.

        Parameters:
        - `instance` (Category): The existing category instance to update.
        - `validated_data` (dict): Validated data for updating the category.

        Returns:
        - `Category`: The updated category instance.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.

    Fields:
    - `id`: The unique identifier for the product.
    - `name`: The name of the product.
    - `description`: The description of the product.
    - `image`: The image URL or file path of the product.
    - `price`: The price of the product.
    - `category`: The associated category (serialized using CategorySerializer).
    - `stock`: The stock quantity of the product.
    """
    category = CategorySerializer()  # Include CategorySerializer for nested serialization

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'price', 'category', 'stock']
        
    def create(self, validated_data):
        """
        Create a new product instance.

        Parameters:
        - `validated_data` (dict): Validated data for creating the product.

        Returns:
        - `Product`: The created product instance.
        """
        # Extract and create category separately to avoid errors
        category_data = validated_data.pop('category', None)
        category_instance = Category.objects.create(**category_data)
        
        # Now, create the product with the category instance
        validated_data['category'] = category_instance
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing product instance.

        Parameters:
        - `instance` (Product): The existing product instance to update.
        - `validated_data` (dict): Validated data for updating the product.

        Returns:
        - `Product`: The updated product instance.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        
        # Update category if provided
        category_data = validated_data.get('category', {})
        instance.category.name = category_data.get('name', instance.category.name)
        instance.category.save()
        
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance
