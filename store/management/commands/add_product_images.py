from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.files import File
import requests
import os
from store.models import Product
from io import BytesIO


class Command(BaseCommand):
    help = 'Add real product images from Unsplash'

    def handle(self, *args, **options):
        self.stdout.write('Adding real product images...')
        
        # Product image mappings - using Unsplash images
        product_images = {
            # Men's T-Shirts
            'classic-cotton-tshirt-men': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&h=500&fit=crop',
            'graphic-print-tshirt-men': 'https://images.unsplash.com/photo-1503341504253-dff4815485f1?w=500&h=500&fit=crop',
            'vneck-tshirt-men': 'https://images.unsplash.com/photo-1434389677669-e08b5c80b8b0?w=500&h=500&fit=crop',
            
            # Women's T-Shirts
            'fitted-cotton-tshirt-women': 'https://images.unsplash.com/photo-1489980557514-251d61e3eeb6?w=500&h=500&fit=crop',
            'crop-top-tshirt-women': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=500&h=500&fit=crop',
            
            # Men's Jeans
            'slim-fit-jeans-men': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=500&h=500&fit=crop',
            'straight-leg-jeans-men': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=500&h=500&fit=crop',
            
            # Women's Jeans
            'high-waist-skinny-jeans-women': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=500&h=500&fit=crop',
            'mom-fit-jeans-women': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=500&h=500&fit=crop',
            
            # Women's Dresses
            'summer-floral-dress-women': 'https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=500&h=500&fit=crop',
            'little-black-dress-women': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=500&h=500&fit=crop',
            'casual-maxi-dress-women': 'https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=500&h=500&fit=crop',
            
            # Men's Shirts
            'oxford-button-down-shirt-men': 'https://images.unsplash.com/photo-1596755094514-f87e34085b39?w=500&h=500&fit=crop',
            'polo-shirt-men': 'https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=500&h=500&fit=crop',
            
            # Women's Shirts
            'silk-blouse-women': 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=500&h=500&fit=crop',
            'chiffon-top-women': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=500&h=500&fit=crop',
            
            # Men's Hoodies
            'fleece-hoodie-men': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500&h=500&fit=crop',
            'zip-up-hoodie-men': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500&h=500&fit=crop',
            
            # Women's Hoodies
            'oversized-hoodie-women': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500&h=500&fit=crop',
            
            # Men's Jackets
            'denim-jacket-men': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=500&h=500&fit=crop',
            'bomber-jacket-men': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=500&h=500&fit=crop',
            
            # Women's Jackets
            'blazer-jacket-women': 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=500&h=500&fit=crop',
            'leather-jacket-women': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=500&h=500&fit=crop',
        }
        
        for slug, image_url in product_images.items():
            try:
                product = Product.objects.get(slug=slug)
                
                # Download image
                response = requests.get(image_url, timeout=10)
                if response.status_code == 200:
                    # Create image file
                    image_name = f"{slug}.jpg"
                    image_file = ContentFile(response.content, name=image_name)
                    
                    # Save image to product
                    product.image.save(image_name, image_file, save=True)
                    
                    self.stdout.write(
                        self.style.SUCCESS(f'Added image for: {product.name}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Failed to download image for: {product.name}')
                    )
                    
            except Product.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'Product not found: {slug}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error processing {slug}: {str(e)}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully added product images!')
        ) 