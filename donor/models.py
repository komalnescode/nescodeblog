from django.db import models
# from django.utils import timezone
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
CATEGORY= [
    ('em', 'Electronics Material'),
    ('cf', 'Cloths_Food'),
    ('edum', 'Education Material'),
    ('ot', 'Other'),
    ]
CITY= [
	('Bgm', 'Belgaum'),
	('Bgr', 'Banglore'),
	('Hub', 'Hubali'),
	('Dhr', 'Dharwad'),
	('Pun', 'Pune'),
	('Mum', 'Mumbai'),
	]


class Donors(models.Model):
	category = models.CharField(max_length=4, choices=CATEGORY)
	cat_id = models.AutoField(primary_key=True)
	p_no = models.PositiveIntegerField()
	p_name = models.CharField(max_length=20)
	desc = models.TextField()
	img = models.ImageField(upload_to = 'media/pic_folder/', default = 'pic_folder/None/no-img.jpg')
	donor_name = models.CharField(max_length=50)
	phno = models.CharField(max_length=10)
	price = models.PositiveIntegerField()
	h_no = models.PositiveIntegerField()
	city = models.CharField(max_length=3, choices=CITY)
	state = models.CharField(max_length=20)
	pincode = models.CharField(max_length=6)
	country = models.CharField(max_length=20, default="India", editable="False")

	def __str__(self):
		return self.category

	# def __str__(self):
 #    	return self.p_name