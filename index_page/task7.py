from index_page.models import Product

#Inserting a new record
new_record = Product(Product="Ink", Price="$15")
new_record.save()

#Getting all records
Product.objects.all()

#Filtering products by their name
Product.objects.values_list('Product', flat=True).distinct()

#Getting a single record from the product table
Product.objects.get(pk=2)

#Changing a product price
x = Product.objects.get(pk=2)
x.Price="$35"
x.save()

