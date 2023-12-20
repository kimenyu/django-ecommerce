from rest_framework import serializers
from .models import Product, Category, Cart, CartItem, ContactInfo, Profile, Order
from accounts.models import UserAccount

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

class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for CartItem model.

    Fields:
    - `id`: The unique identifier for the cart item.
    - `cart`: The associated cart (serialized using CartSerializer).
    - `product`: The associated product (serialized using ProductSerializer).
    - `quantity`: The quantity of the product in the cart.
    """
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']
        
    def create(self, validated_data):
        """
        Create a new cart item instance.

        Parameters:
        - `validated_data` (dict): Validated data for creating the cart item.

        Returns:
        - `CartItem`: The created cart item instance.
        """
        return CartItem.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing cart item instance.

        Parameters:
        - `instance` (CartItem): The existing cart item instance to update.
        - `validated_data` (dict): Validated data for updating the cart item.

        Returns:
        - `CartItem`: The updated cart item instance.
        """
        instance.cart = validated_data.get('cart', instance.cart)
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
    
class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for Cart model.

    Fields:
    - `id`: The unique identifier for the cart.
    - `user`: The associated user (serialized using UserAccountSerializer).
    - `created_at`: The date and time when the cart was created.
    - `items`: The associated cart items (serialized using CartItemSerializer).
    """
    user = serializers.PrimaryKeyRelatedField(queryset=UserAccount.objects.all())
    items = CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']
        
    def create(self, validated_data):
        """
        Create a new cart instance.

        Parameters:
        - `validated_data` (dict): Validated data for creating the cart.

        Returns:
        - `Cart`: The created cart instance.
        """
        return Cart.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing cart instance.

        Parameters:
        - `instance` (Cart): The existing cart instance to update.
        - `validated_data` (dict): Validated data for updating the cart.

        Returns:
        - `Cart`: The updated cart instance.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
    
class ContactInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for ContactInfo model.

    Fields:
    - `id`: The unique identifier for the contact info.
    - `user`: The associated user (serialized using UserAccountSerializer).
    - `email`: The email address of the user.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=UserAccount.objects.all())
    
    class Meta:
        model = ContactInfo
        fields = ['id', 'user', 'email']
        
    def create(self, validated_data):
        """
        Create a new contact info instance.

        Parameters:
        - `validated_data` (dict): Validated data for creating the contact info.

        Returns:
        - `ContactInfo`: The created contact info instance.
        """
        return ContactInfo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing contact info instance.

        Parameters:
        - `instance` (ContactInfo): The existing contact info instance to update.
        - `validated_data` (dict): Validated data for updating the contact info.

        Returns:
        - `ContactInfo`: The updated contact info instance.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile model.

    Fields:
    - `id`: The unique identifier for the profile.
    - `user`: The associated user (serialized using UserAccountSerializer).
    - `first_name`: The first name of the user.
    - `last_name`: The last name of the user.
    - `contact_info`: The associated contact info (serialized using ContactInfoSerializer).
    - `phone_number`: The phone number of the user.
    - `address`: The address of the user.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=UserAccount.objects.all())
    contact_info = ContactInfoSerializer()
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'contact_info', 'phone_number', 'address']
        
    def create(self, validated_data):
        """
        Create a new profile instance.

        Parameters:
        - `validated_data` (dict): Validated data for creating the profile.

        Returns:
        - `Profile`: The created profile instance.
        """
        # Extract and create contact info separately to avoid errors
        contact_info_data = validated_data.pop('contact_info', None)
        contact_info_instance = ContactInfo.objects.create(**contact_info_data)
        
        # Now, create the profile with the contact info instance
        validated_data['contact_info'] = contact_info_instance
        return Profile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing profile instance.

        Parameters:
        - `instance` (Profile): The existing profile instance to update.
        - `validated_data` (dict): Validated data for updating the profile.

        Returns:
        - `Profile`: The updated profile instance.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        
        # Update contact info if provided
        contact_info_data = validated_data.get('contact_info', {})
        instance.contact_info.email = contact_info_data.get('email', instance.contact_info.email)
        instance.contact_info.save()
        
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.

    Fields:
    - `id`: The unique identifier for the order.
    - `user`: The associated user (serialized using UserAccountSerializer).
    - `cart`: The associated cart (serialized using CartSerializer).
    - `total_amount`: The total amount of the order.
    - `created_at`: The date and time when the order was created.
    - `status`: The status of the order.
    - `contact_info`: The associated contact info (serialized using ContactInfoSerializer).
    """
    user = serializers.PrimaryKeyRelatedField(queryset=UserAccount.objects.all())
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    contact_info = ContactInfoSerializer()
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'cart', 'total_amount', 'created_at', 'status', 'contact_info']
        
    def create(self, validated_data):
        """
        Create a new order instance.

        Parameters:
        - `validated_data` (dict): Validated data for creating the order.

        Returns:
        - `Order`: The created order instance.
        """
        # Extract and create contact info separately to avoid errors
        contact_info_data = validated_data.pop('contact_info', None)
        contact_info_instance = ContactInfo.objects.create(**contact_info_data)
        
        # Now, create the order with the contact info instance
        validated_data['contact_info'] = contact_info_instance
        return Order.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing order instance.

        Parameters:
        - `instance` (Order): The existing order instance to update.
        - `validated_data` (dict): Validated data for updating the order.

        Returns:
        - `Order`: The updated order instance.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.cart = validated_data.get('cart', instance.cart)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.status = validated_data.get('status', instance.status)
        
        # Update contact info if provided
        contact_info_data = validated_data.get('contact_info', {})
        instance.contact_info.email = contact_info_data.get('email', instance.contact_info.email)
        instance.contact_info.save()
        
        instance.save()
        return instance
