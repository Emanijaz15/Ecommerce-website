from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from store.models import Category, Product
import random


class Command(BaseCommand):
    help = 'Populate the database with dummy clothing products'

    def handle(self, *args, **options):
        self.stdout.write('Creating categories...')
        
        # Create categories
        categories_data = [
            {
                'name': 'T-Shirts',
                'slug': 't-shirts',
                'description': 'Comfortable and stylish t-shirts for everyday wear'
            },
            {
                'name': 'Jeans',
                'slug': 'jeans',
                'description': 'Classic denim jeans in various styles and fits'
            },
            {
                'name': 'Dresses',
                'slug': 'dresses',
                'description': 'Elegant dresses for special occasions and casual wear'
            },
            {
                'name': 'Shirts',
                'slug': 'shirts',
                'description': 'Formal and casual shirts for professional and casual settings'
            },
            {
                'name': 'Hoodies',
                'slug': 'hoodies',
                'description': 'Warm and comfortable hoodies for cold weather'
            },
            {
                'name': 'Jackets',
                'slug': 'jackets',
                'description': 'Stylish jackets for all seasons'
            }
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        self.stdout.write('Creating products...')
        
        # Product data
        products_data = [
            # Men's T-Shirts
            {
                'name': 'Classic Cotton T-Shirt',
                'slug': 'classic-cotton-tshirt-men',
                'description': 'Premium cotton t-shirt with a comfortable fit. Perfect for everyday wear.',
                'price': 24.99,
                'original_price': 29.99,
                'category': 't-shirts',
                'gender': 'M',
                'stock': 50
            },
            {
                'name': 'Graphic Print T-Shirt',
                'slug': 'graphic-print-tshirt-men',
                'description': 'Stylish graphic print t-shirt with unique designs. Made from soft cotton.',
                'price': 19.99,
                'category': 't-shirts',
                'gender': 'M',
                'stock': 35
            },
            {
                'name': 'V-Neck T-Shirt',
                'slug': 'vneck-tshirt-men',
                'description': 'Elegant v-neck t-shirt perfect for layering or casual wear.',
                'price': 22.99,
                'original_price': 27.99,
                'category': 't-shirts',
                'gender': 'M',
                'stock': 40
            },
            
            # Women's T-Shirts
            {
                'name': 'Fitted Cotton T-Shirt',
                'slug': 'fitted-cotton-tshirt-women',
                'description': 'Flattering fitted t-shirt made from premium cotton. Available in multiple colors.',
                'price': 21.99,
                'original_price': 26.99,
                'category': 't-shirts',
                'gender': 'W',
                'stock': 45
            },
            {
                'name': 'Crop Top T-Shirt',
                'slug': 'crop-top-tshirt-women',
                'description': 'Trendy crop top t-shirt perfect for summer styling.',
                'price': 18.99,
                'category': 't-shirts',
                'gender': 'W',
                'stock': 30
            },
            
            # Men's Jeans
            {
                'name': 'Slim Fit Jeans',
                'slug': 'slim-fit-jeans-men',
                'description': 'Modern slim fit jeans with stretch denim for maximum comfort.',
                'price': 59.99,
                'original_price': 79.99,
                'category': 'jeans',
                'gender': 'M',
                'stock': 25
            },
            {
                'name': 'Straight Leg Jeans',
                'slug': 'straight-leg-jeans-men',
                'description': 'Classic straight leg jeans with a timeless fit.',
                'price': 54.99,
                'category': 'jeans',
                'gender': 'M',
                'stock': 30
            },
            
            # Women's Jeans
            {
                'name': 'High Waist Skinny Jeans',
                'slug': 'high-waist-skinny-jeans-women',
                'description': 'Flattering high waist skinny jeans with stretch denim.',
                'price': 64.99,
                'original_price': 84.99,
                'category': 'jeans',
                'gender': 'W',
                'stock': 28
            },
            {
                'name': 'Mom Fit Jeans',
                'slug': 'mom-fit-jeans-women',
                'description': 'Trendy mom fit jeans with a relaxed yet stylish silhouette.',
                'price': 59.99,
                'category': 'jeans',
                'gender': 'W',
                'stock': 22
            },
            
            # Women's Dresses
            {
                'name': 'Summer Floral Dress',
                'slug': 'summer-floral-dress-women',
                'description': 'Beautiful floral print dress perfect for summer occasions.',
                'price': 49.99,
                'original_price': 69.99,
                'category': 'dresses',
                'gender': 'W',
                'stock': 20
            },
            {
                'name': 'Little Black Dress',
                'slug': 'little-black-dress-women',
                'description': 'Timeless little black dress for elegant occasions.',
                'price': 79.99,
                'category': 'dresses',
                'gender': 'W',
                'stock': 15
            },
            {
                'name': 'Casual Maxi Dress',
                'slug': 'casual-maxi-dress-women',
                'description': 'Comfortable maxi dress perfect for casual outings.',
                'price': 44.99,
                'category': 'dresses',
                'gender': 'W',
                'stock': 18
            },
            
            # Men's Shirts
            {
                'name': 'Oxford Button-Down Shirt',
                'slug': 'oxford-button-down-shirt-men',
                'description': 'Classic oxford button-down shirt perfect for business casual.',
                'price': 39.99,
                'original_price': 49.99,
                'category': 'shirts',
                'gender': 'M',
                'stock': 25
            },
            {
                'name': 'Polo Shirt',
                'slug': 'polo-shirt-men',
                'description': 'Comfortable polo shirt made from breathable cotton.',
                'price': 29.99,
                'category': 'shirts',
                'gender': 'M',
                'stock': 35
            },
            
            # Women's Shirts
            {
                'name': 'Silk Blouse',
                'slug': 'silk-blouse-women',
                'description': 'Elegant silk blouse perfect for professional settings.',
                'price': 69.99,
                'original_price': 89.99,
                'category': 'shirts',
                'gender': 'W',
                'stock': 20
            },
            {
                'name': 'Chiffon Top',
                'slug': 'chiffon-top-women',
                'description': 'Lightweight chiffon top with a feminine silhouette.',
                'price': 34.99,
                'category': 'shirts',
                'gender': 'W',
                'stock': 25
            },
            
            # Men's Hoodies
            {
                'name': 'Fleece Hoodie',
                'slug': 'fleece-hoodie-men',
                'description': 'Warm fleece hoodie perfect for cold weather.',
                'price': 44.99,
                'original_price': 59.99,
                'category': 'hoodies',
                'gender': 'M',
                'stock': 30
            },
            {
                'name': 'Zip-Up Hoodie',
                'slug': 'zip-up-hoodie-men',
                'description': 'Versatile zip-up hoodie with front pockets.',
                'price': 39.99,
                'category': 'hoodies',
                'gender': 'M',
                'stock': 25
            },
            
            # Women's Hoodies
            {
                'name': 'Oversized Hoodie',
                'slug': 'oversized-hoodie-women',
                'description': 'Comfortable oversized hoodie perfect for lounging.',
                'price': 42.99,
                'original_price': 57.99,
                'category': 'hoodies',
                'gender': 'W',
                'stock': 28
            },
            
            # Men's Jackets
            {
                'name': 'Denim Jacket',
                'slug': 'denim-jacket-men',
                'description': 'Classic denim jacket with a timeless style.',
                'price': 74.99,
                'original_price': 94.99,
                'category': 'jackets',
                'gender': 'M',
                'stock': 20
            },
            {
                'name': 'Bomber Jacket',
                'slug': 'bomber-jacket-men',
                'description': 'Stylish bomber jacket with ribbed cuffs and hem.',
                'price': 89.99,
                'category': 'jackets',
                'gender': 'M',
                'stock': 15
            },
            
            # Women's Jackets
            {
                'name': 'Blazer Jacket',
                'slug': 'blazer-jacket-women',
                'description': 'Professional blazer jacket perfect for office wear.',
                'price': 89.99,
                'original_price': 109.99,
                'category': 'jackets',
                'gender': 'W',
                'stock': 18
            },
            {
                'name': 'Leather Jacket',
                'slug': 'leather-jacket-women',
                'description': 'Edgy leather jacket with a rebellious style.',
                'price': 149.99,
                'category': 'jackets',
                'gender': 'W',
                'stock': 12
            }
        ]
        
        # Create a simple placeholder image
        placeholder_image = ContentFile(
            b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==',
            name='placeholder.png'
        )
        
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults={
                    'name': product_data['name'],
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'original_price': product_data.get('original_price'),
                    'category': categories[product_data['category']],
                    'gender': product_data['gender'],
                    'stock': product_data['stock'],
                    'image': placeholder_image
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with dummy products!')
        ) 