from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from store.models import Product
import base64


class Command(BaseCommand):
    help = 'Add fallback images for products that failed to download'

    def handle(self, *args, **options):
        self.stdout.write('Adding fallback images...')
        
        # Create a simple colored placeholder image
        # This is a 1x1 pixel PNG with a light gray color
        placeholder_png = base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=='
        )
        
        # Products that need fallback images
        fallback_products = [
            'vneck-tshirt-men',
            'high-waist-skinny-jeans-women', 
            'oxford-button-down-shirt-men',
            'oversized-hoodie-women',
            'denim-jacket-men',
            'bomber-jacket-men',
            'leather-jacket-women'
        ]
        
        for slug in fallback_products:
            try:
                product = Product.objects.get(slug=slug)
                
                # Create a colored placeholder based on product type
                if 'tshirt' in slug:
                    color = '#3498db'  # Blue for t-shirts
                elif 'jeans' in slug:
                    color = '#2c3e50'  # Dark blue for jeans
                elif 'shirt' in slug:
                    color = '#e74c3c'  # Red for shirts
                elif 'hoodie' in slug:
                    color = '#f39c12'  # Orange for hoodies
                elif 'jacket' in slug:
                    color = '#8e44ad'  # Purple for jackets
                else:
                    color = '#95a5a6'  # Gray default
                
                # Create a simple SVG placeholder
                svg_content = f'''<svg width="500" height="500" xmlns="http://www.w3.org/2000/svg">
                    <rect width="500" height="500" fill="{color}"/>
                    <text x="250" y="250" font-family="Arial" font-size="24" fill="white" text-anchor="middle" dominant-baseline="middle">
                        {product.name}
                    </text>
                </svg>'''
                
                # Save as SVG file
                image_name = f"{slug}_fallback.svg"
                image_file = ContentFile(svg_content.encode('utf-8'), name=image_name)
                
                product.image.save(image_name, image_file, save=True)
                
                self.stdout.write(
                    self.style.SUCCESS(f'Added fallback image for: {product.name}')
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
            self.style.SUCCESS('Successfully added fallback images!')
        ) 