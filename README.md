# Fashion Store - Django E-commerce Website

A modern, responsive e-commerce website built with Django for men's and women's clothing. Features a beautiful UI with Bootstrap 5, shopping cart functionality, product filtering, and search capabilities.

## Features

- 🛍️ **Product Catalog**: Browse men's and women's clothing with detailed product pages
- 🔍 **Search & Filter**: Search products and filter by category, gender, and price
- 🛒 **Shopping Cart**: Add/remove items, update quantities, and view cart summary
- 💳 **Checkout Process**: Complete checkout flow with shipping and payment forms
- 📱 **Responsive Design**: Mobile-friendly design that works on all devices
- 🎨 **Modern UI**: Beautiful Bootstrap 5 design with smooth animations
- ⚡ **Fast & Lightweight**: Optimized for performance and user experience

## Product Categories

- **T-Shirts**: Comfortable and stylish t-shirts for everyday wear
- **Jeans**: Classic denim jeans in various styles and fits
- **Dresses**: Elegant dresses for special occasions and casual wear
- **Shirts**: Formal and casual shirts for professional and casual settings
- **Hoodies**: Warm and comfortable hoodies for cold weather
- **Jackets**: Stylish jackets for all seasons

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, Font Awesome
- **Database**: SQLite (can be easily changed to PostgreSQL/MySQL)
- **Image Handling**: Pillow
- **Forms**: Django Crispy Forms with Bootstrap 5

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Project

```bash
# If you have git installed
git clone <repository-url>
cd ecommerce

# Or simply extract the downloaded files to your desired directory
```

### Step 2: Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 6: Populate with Dummy Data

```bash
python manage.py populate_products
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

### Step 8: Access the Website

Open your browser and go to:
- **Main Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Project Structure

```
ecommerce/
├── ecommerce/                 # Main Django project
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── store/                    # Main app
│   ├── __init__.py
│   ├── admin.py             # Admin interface
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   └── management/          # Custom management commands
│       └── commands/
│           └── populate_products.py
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   └── store/              # Store app templates
│       ├── home.html       # Home page
│       ├── product_list.html # Product listing
│       ├── product_detail.html # Product detail
│       ├── cart.html       # Shopping cart
│       └── checkout.html   # Checkout page
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User uploaded files
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Key Features Explained

### 1. Product Management
- Products are organized by categories and gender
- Each product has images, descriptions, prices, and stock levels
- Support for original prices and discount calculations

### 2. Shopping Cart
- Session-based cart for guest users
- User-based cart for registered users
- Real-time quantity updates and price calculations
- AJAX-powered cart interactions

### 3. Search & Filtering
- Search products by name, description, or category
- Filter by gender (Men/Women)
- Filter by product category
- Sort by price, name, or newest first

### 4. Responsive Design
- Mobile-first approach with Bootstrap 5
- Responsive product grid
- Touch-friendly navigation
- Optimized for all screen sizes

### 5. User Experience
- Clean, modern interface
- Smooth hover animations
- Loading states and feedback
- Intuitive navigation

## Customization

### Adding New Products

1. **Via Admin Panel**: Go to http://127.0.0.1:8000/admin/ and add products through the admin interface

2. **Via Management Command**: Modify `store/management/commands/populate_products.py` and run:
   ```bash
   python manage.py populate_products
   ```

### Styling Customization

The website uses CSS custom properties for easy theming. Main colors are defined in `templates/base.html`:

```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #e74c3c;
    --accent-color: #3498db;
    --light-gray: #ecf0f1;
    --dark-gray: #2c3e50;
}
```

### Database Configuration

To use a different database (PostgreSQL, MySQL), update the `DATABASES` setting in `ecommerce/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Deployment

### Production Settings

Before deploying, update `ecommerce/settings.py`:

1. Set `DEBUG = False`
2. Update `ALLOWED_HOSTS` with your domain
3. Configure your production database
4. Set up static file serving
5. Use environment variables for sensitive settings

### Static Files

Collect static files for production:
```bash
python manage.py collectstatic
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions:

1. Check the Django documentation
2. Review the code comments
3. Create an issue in the repository

## Future Enhancements

- User authentication and accounts
- Order history and tracking
- Payment gateway integration
- Product reviews and ratings
- Wishlist functionality
- Email notifications
- Advanced search filters
- Product variants (size, color)
- Inventory management
- Analytics dashboard

---

**Happy Shopping! 🛍️** 