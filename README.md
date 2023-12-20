# Django Ecommerce API

Welcome to the Django Ecommerce API repository! This Django REST Framework project serves as an ecommerce platform.

## Getting Started

To use this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/kimenyu/django-ecommerce.git
    ```

2. Navigate to the backend folder:
    ```bash
    cd django-ecommerce/backend
    ```

3. Navigate to the ShopZone directory:
    ```bash
    cd ShopZone
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Cart

#### List Cart Items

- **Endpoint:** `/products/cart/`
- **Method:** GET
- **Description:** ListAPIView for retrieving a list of cart items.
  - HTTP Methods:
    - GET: Retrieve a list of cart items.

### Cart Item

#### Create Cart Item

- **Endpoint:** `/products/cart-item/create/`
- **Method:** POST
- **Description:** CreateAPIView for creating a new cart item.
  - HTTP Methods:
    - POST: Create a new cart item.
  - Request Data:
    - JSON object containing cart item details.
  - Fields:
    - `cart` (required, form): Cart ID (integer).
    - `product` (required, form): Product ID (integer).
    - `quantity` (form): Quantity (integer).

#### Delete Cart Item

- **Endpoint:** `/products/cart-item/delete/{id}/`
- **Method:** DELETE
- **Description:** DestroyAPIView for deleting a specific cart item.
  - HTTP Methods:
    - DELETE: Delete a specific cart item.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this cart item.

#### Update Cart Item

- **Endpoint:** `/products/cart-item/update/{id}/`
- **Method:** PUT
- **Description:** UpdateAPIView for updating details of a specific cart item.
  - HTTP Methods:
    - PUT/PATCH: Update details of a specific cart item.
  - Request Data:
    - JSON object containing updated cart item details.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this cart item.
    - `cart` (required, form): Cart ID (integer).
    - `product` (required, form): Product ID (integer).
    - `quantity` (form): Quantity (integer).

### Contact Info

#### Create Contact Info

- **Endpoint:** `/products/contact-info/create/`
- **Method:** POST
- **Description:** CreateAPIView for creating a new contact info.
  - HTTP Methods:
    - POST: Create a new contact info.
  - Request Data:
    - JSON object containing contact info details.
  - Fields:
    - `user` (required, form): User ID (integer).
    - `email` (form): Email (string).

#### Delete Contact Info

- **Endpoint:** `/products/contact-info/delete/{id}/`
- **Method:** DELETE
- **Description:** DestroyAPIView for deleting a specific contact info.
  - HTTP Methods:
    - DELETE: Delete a specific contact info.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this contact info.

#### Retrieve Contact Info Details

- **Endpoint:** `/products/contact-info/detail/{id}/`
- **Method:** GET
- **Description:** RetrieveAPIView for retrieving details of a specific contact info.
  - HTTP Methods:
    - GET: Retrieve details of a specific contact info.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this contact info.

#### List Contact Infos

- **Endpoint:** `/products/contact-info/list/`
- **Method:** GET
- **Description:** ListAPIView for retrieving a list of contact infos.
  - HTTP Methods:
    - GET: Retrieve a list of contact infos.

#### Update Contact Info

- **Endpoint:** `/products/contact-info/update/{id}/`
- **Method:** PUT
- **Description:** UpdateAPIView for updating details of a specific contact info.
  - HTTP Methods:
    - PUT/PATCH: Update details of a specific contact info.
  - Request Data:
    - JSON object containing updated contact info details.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this contact info.
    - `user` (required, form): User ID (integer).
    - `email` (form): Email (string).

### Product

#### Create Product

- **Endpoint:** `/products/create/`
- **Method:** POST
- **Description:** CreateAPIView for creating a new product.
  - HTTP Methods:
    - POST: Create a new product.
  - Request Data:
    - JSON object containing product details.
  - Fields:
    - `name` (required, form): Name (string).
    - `description` (required, form): Description (string).
    - `image` (required, form): Image (string).
    - `price` (required, form): Price (number).
    - `category` (required, form): Category (object).
    - `stock` (form): Stock (integer).

#### Delete Product

- **Endpoint:** `/products/delete/{id}/`
- **Method:** DELETE
- **Description:** DestroyAPIView for deleting a specific product.
  - HTTP Methods:
    - DELETE: Delete a specific product.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this product.

#### Retrieve Product Details

- **Endpoint:** `/products/detail/{id}/`
- **Method:** GET
- **Description:** RetrieveAPIView for retrieving details of a specific product.
  - HTTP Methods:
    - GET: Retrieve details of a specific product.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this product.

#### List Products

- **Endpoint:** `/products/list/`
- **Method:** GET
- **Description:** ListAPIView for retrieving a list of products.
  - HTTP Methods:
    - GET: Retrieve a list of products.
  - Query Parameters:
    - `name` (optional): Filter products by name.

#### Update Product

- **Endpoint:** `/products/update/{id}/`
- **Method:** PUT
- **Description:** UpdateAPIView for updating details of a specific product.
  - HTTP Methods:
    - PUT/PATCH: Update details of a specific product.
  - Request Data:
    - JSON object containing updated product details.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this product.
    - `name` (form): Name (string).
    - `description` (form): Description (string).
    - `image` (form): Image (string).
    - `price` (form): Price (number).
    - `category` (form): Category (object).
    - `stock` (form): Stock (integer).

### Order

#### Create Order

- **Endpoint:** `/products/order/create/`
- **Method:** POST
- **Description:** CreateAPIView for creating a new order.
  - HTTP Methods:
    - POST: Create a new order.
  - Request Data:
    - JSON object containing order details.
  - Fields:
    - `user` (required, form): User ID (integer).
    - `cart` (required, form): Cart ID (integer).
    - `total_amount` (required, form): Total amount (number).
    - `status` (form): Status (enum: processing, shipped, delivered).
    - `contact_info` (required, form): Contact info (object).

#### Delete Order

- **Endpoint:** `/products/order/delete/{id}/`
- **Method:** DELETE
- **Description:** DestroyAPIView for deleting a specific order.
  - HTTP Methods:
    - DELETE: Delete a specific order.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this order.

#### Retrieve Order Details

- **Endpoint:** `/products/order/detail/{id}/`
- **Method:** GET
- **Description:** RetrieveAPIView for retrieving details of a specific order.
  - HTTP Methods:
    - GET: Retrieve details of a specific order.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this order.

#### List Orders

- **Endpoint:** `/products/order/list/`
- **Method:** GET
- **Description:** ListAPIView for retrieving a list of orders.
  - HTTP Methods:
    - GET: Retrieve a list of orders.

#### Update Order

- **Endpoint:** `/products/order/update/{id}/`
- **Method:** PUT
- **Description:** UpdateAPIView for updating details of a specific order.
  - HTTP Methods:
    - PUT/PATCH: Update details of a specific order.
  - Request Data:
    - JSON object containing updated order details.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this order.
    - `user` (required, form): User ID (integer).
    - `cart` (required, form): Cart ID (integer).
    - `total_amount` (required, form): Total amount (number).
    - `status` (form): Status (enum: processing, shipped, delivered).
    - `contact_info` (required, form): Contact info (object).

### Profile

#### Create Profile

- **Endpoint:** `/products/profile/create/`
- **Method:** POST
- **Description:** CreateAPIView for creating a new profile.
  - HTTP Methods:
    - POST: Create a new profile.
  - Request Data:
    - JSON object containing profile details.
  - Fields:
    - `user` (required, form): User ID (integer).
    - `first_name` (form): First name (string).
    - `last_name` (form): Last name (string).
    - `contact_info` (required, form): Contact info (object).
    - `phone_number` (form): Phone number (string).
    - `address` (form): Address (string).

#### Delete Profile

- **Endpoint:** `/products/profile/delete/{id}/`
- **Method:** DELETE
- **Description:** DestroyAPIView for deleting a specific profile.
  - HTTP Methods:
    - DELETE: Delete a specific profile.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this profile.

#### Retrieve Profile Details

- **Endpoint:** `/products/profile/detail/{id}/`
- **Method:** GET
- **Description:** RetrieveAPIView for retrieving details of a specific profile.
  - HTTP Methods:
    - GET: Retrieve details of a specific profile.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this profile.

#### List Profiles

- **Endpoint:** `/products/profile/`
- **Method:** GET
- **Description:** ListAPIView for retrieving a list of profiles.
  - HTTP Methods:
    - GET: Retrieve a list of profiles.

#### Update Profile

- **Endpoint:** `/products/profile/update/{id}/`
- **Method:** PUT
- **Description:** UpdateAPIView for updating details of a specific profile.
  - HTTP Methods:
    - PUT/PATCH: Update details of a specific profile.
  - Request Data:
    - JSON object containing updated profile details.
  - Fields:
    - `id` (required, path): ID (integer) - A unique integer value identifying this profile.
    - `user` (required, form): User ID (integer).
    - `first_name` (form): First name (string).
    - `last_name` (form): Last name (string).
    - `contact_info` (required, form): Contact info (object).
    - `phone_number` (form): Phone number (string).
    - `address` (form): Address (string).

## Server Information

The API is served at: [http://127.0.0.1:8000/schema/](http://127.0.0.1:8000/schema/)
