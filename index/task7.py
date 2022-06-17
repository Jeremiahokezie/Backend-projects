<<<<<<< HEAD:index/task7.py
""""from home.models import Product
=======
from index_page.models import Product
>>>>>>> 811cdcfd41ac68f99ab0fd3e2ef7a17aea772afc:index_page/task7.py

#Inserting a new record
new_record = Product(Product="Ink", Price="$15")
new_record.save()

#Getting all records
Product.objects.all()

#Filtering products by their name
Product.objects.get(Product="Ink")
Product.objects.get(Product="Titus")

#Getting a single record from the product table
Product.objects.get(pk=2)

#Changing a product price
x = Product.objects.get(pk=2)
x.Price="$35"
x.save()"""

