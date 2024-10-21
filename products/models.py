from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class CategoryModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class TagModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Tag Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class BrandModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Brand Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class ColorModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Color Name"), unique=True)
    code = models.CharField(max_length=100, verbose_name=_("code"), unique=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")


class SizeModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Size Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")


class ProductModel(BaseModel):
    image1 = models.ImageField(verbose_name=_("Image 1"), upload_to="images/")
    image2 = models.ImageField(verbose_name=_("Image 2"), upload_to="images/")
    short_description = models.TextField(verbose_name=_("Short Description"))
    long_description = models.TextField(verbose_name=_("Long Description"))
    in_stock = models.BooleanField(verbose_name=_("In stock"), default=True)
    sku = models.CharField(max_length=100, verbose_name=_("SKU"), unique=True)
    quantity = models.IntegerField(verbose_name=_("Quantity"), default=1)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    discount = models.FloatField(default=0, verbose_name=_("Discount"), validators=[MinValueValidator(0), MaxValueValidator(100)])
    real_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Real Price"), default=0.00)

    category = models.ManyToManyField(CategoryModel, related_name="products")
    tag = models.ManyToManyField(TagModel, related_name="products")
    brands = models.ForeignKey(BrandModel, related_name="products", on_delete=models.CASCADE)
    color = models.ManyToManyField(ColorModel, related_name="products")
    size = models.ManyToManyField(SizeModel, related_name="products")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'products'
        verbose_name = 'Product'


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_("Image"), upload_to="products/images/")
