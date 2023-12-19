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

### Create Product

- **Endpoint:** `/products/create/`
- **Method:** POST
- **Description:** Create a new product.
- **Request Data:** JSON object containing product details.

### Delete Product

- **Endpoint:** `/products/delete/{id}/`
- **Method:** DELETE
- **Description:** Delete a specific product.
- **Parameters:**
  - `id` (path): A unique integer value identifying the product.

### Retrieve Product Details

- **Endpoint:** `/products/detail/{id}/`
- **Method:** GET
- **Description:** Retrieve details of a specific product.
- **Parameters:**
  - `id` (path): A unique integer value identifying the product.

### List Products

- **Endpoint:** `/products/list/`
- **Method:** GET
- **Description:** Retrieve a list of products.
- **Query Parameters:**
  - `name` (optional): Filter products by name.

### Update Product

- **Endpoint:** `/products/update/{id}/`
- **Method:** PUT/PATCH
- **Description:** Update details of a specific product.
- **Request Data:** JSON object containing updated product details.
- **Parameters:**
  - `id` (path): A unique integer value identifying the product.

## Server Information

The API is served at: [http://127.0.0.1:8000/schema/](http://127.0.0.1:8000/schema/)

Feel free to explore and contribute to this Django Ecommerce API!
