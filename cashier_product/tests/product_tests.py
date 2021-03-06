from passlib.hash import oracle10
from database.models.category import SubCategory
import unittest
import random
from database.models.category import Category
from database.models.product import Product, ProductImage
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files import File
import logging
from django.urls import reverse, reverse_lazy
from faker import Faker
from cashier_user.tests.user_tests import tokens, readme

faker = Faker()
_dat = {}


class Producttests(unittest.TestCase):
    def setUp(self):
        self.e = APIClient()
        self.logger = logging.getLogger(__name__)
        self.name = ""

    def test_category(self):
        self.logger.critical("category tests")

    @unittest.skipIf(not tokens, "tokens is expires")
    def test_category_get_all(self):
        urls = reverse("all-category")
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.get(urls, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("get all category : %s" % response.data)

    @unittest.skipIf(Category.objects.count() == 0, "category not have data")
    @unittest.skipIf(not tokens, "tokens is expires")
    def test_category_get_detail(self):
        category = Category.objects.first()
        urls = reverse("category-detail", args=[category.id])
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.get(urls, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("get detail category")

    @unittest.skipIf(not tokens, "tokens is expires")
    def test_category_create(self):
        urls = reverse("category-list")
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        data = {
            "name": faker.name(),
            "author": tokens.get("user").accounts_set.first().id,
        }
        response = self.e.post(urls, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Category has been created")
        self.logger.info("create category")

    @unittest.skipIf(Category.objects.count() == 0, "category not have data")
    @unittest.skipIf(not tokens, "tokens is expires")
    def test_category_destroy(self):
        category = Category.objects.first()
        urls = reverse("category-detail", args=[category.public_id])
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.delete(urls, format="json")
        self.assertEqual(response.data["message"], "Category has been deleted")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("category has been destroy")

    @unittest.skipIf(Category.objects.count() == 0, "category not have data")
    @unittest.skipIf(not tokens, "tokens is expires")
    def test_category_updated(self):
        category = Category.objects.first()
        urls = reverse("category-detail", args=[category.public_id])
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        data = {"name": faker.name()}
        response = self.e.put(urls, data, format="json")
        self.assertEqual(response.data["message"], "Category has been updated")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("category has been updated")

    def test_sub_category(self):
        self.logger.critical("create sub category")

    @unittest.skipIf(Category.objects.count() == 0, "category not have data")
    @unittest.skipIf(not tokens, "tokens is expires")
    def test_sub_category_create(self):
        category = Category.objects.first()
        urls = reverse("category-list")
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        data = {"name": faker.name(), "category": category.id, "types": "sub-category"}
        response = self.e.post(urls, data, format="json")
        self.assertEqual(response.data["message"], "Category has been created")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.logger.info("sub category has been created")

    @unittest.skipIf(SubCategory.objects.count() == 0, "category not have data")
    @unittest.skipIf(not tokens, "tokens is expires")
    def test_sub_category_destroy(self):
        urls = reverse(
            "sub-category-detail", args=[SubCategory.objects.first().public_id]
        )
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.delete(urls, format="json")
        self.assertEqual(response.data["message"], "Category has been deleted")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("sub category has been deleted")

    @unittest.skipIf(SubCategory.objects.count() == 0, "category not have data")
    @unittest.skipIf(not tokens, "tokens is expires")
    def test_sub_category_update(self):
        urls = reverse(
            "sub-category-detail", args=[SubCategory.objects.first().public_id]
        )
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        data = {"name": faker.name()}
        response = self.e.put(urls, data, format="json")
        self.assertEqual(response.data["message"], "Category has been updated")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("sub category has been updated")

    def test_product(self):
        self.logger.critical("product tests")

    @unittest.skipIf(Product.objects.count() == 0, "category not have data")
    @unittest.skipIf(not tokens, "tokens is expires")
    def test_product_get_all(self):
        urls = reverse("all-product")
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.get(urls, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("get all product : %s" % response.data)

    @unittest.skipIf(Product.objects.count() == 0, "category not have data")
    @unittest.skipIf(not tokens, "tokens is expires")
    def test_product_get_detail(self):
        product = Product.objects.first()
        urls = reverse("product-detail", args=[product.id])
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.get(urls, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("get detail product")

    @unittest.skipIf(SubCategory.objects.count() == 0, "category not have data")
    @unittest.skipIf(not tokens, "tokens is expires")
    def test_product_create(self):
        category = SubCategory.objects.first()
        urls = reverse("product-list")
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        description = ""
        for i in faker.paragraphs():
            description += i
        name = faker.name()
        data = {
            "name": name,
            "description": description,
            "sub": category.id,
            "author": tokens.get("user").accounts_set.first().id,
            "stock": random.randint(10, 20),
            "max_stock": random.randint(30, 40),
            "type": faker.name(),
            "price": random.randint(10000, 90000),
            "sell": random.randint(20000, 90000),
            "sku": oracle10.hash(
                name, user=tokens.get("user").accounts_set.first().public_id
            ),
        }
        response = self.e.post(urls, data, format="multipart")
        _dat["public_id"] = response.data["data"].get("public_id")
        self.assertEqual(response.data["message"], "Product has been created")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.logger.info("product has been created")

    @unittest.skipIf(not tokens, "tokens is expires")
    @unittest.skipIf(Product.objects.count() == 0, "product not have data")
    def test_product_destory(self):
        product = Product.objects.first()
        urls = reverse("product-detail", args=[product.public_id])
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.delete(urls, format="json")
        self.assertEqual(response.data["message"], "Product has been deleted")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("product has been deleted")

    @unittest.skipIf(not tokens, "tokens is expires")
    @unittest.skipIf(Product.objects.count() == 0, "product not have data")
    def test_product_update(self):
        product = Product.objects.first()
        urls = reverse("updated-product", args=[product.public_id])
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        description = ""
        for i in faker.paragraphs():
            description += i
        data = {
            "name": faker.name(),
            "description": description,
            "author": tokens.get("user").accounts_set.first().id,
            "stock": random.randint(10, 20),
            "max_stock": random.randint(30, 40),
            "type": faker.name(),
            "price": random.randint(10000, 90000),
            "sell": random.randint(20000, 90000),
            "icons": File(open("IMG_0083.PNG", "rb")),
            "typeId": product.type.all().first().id,
        }
        response = self.e.post(urls, data, format="multipart")
        print(response.data)
        self.assertEqual(response.data["message"], "Product has been updated")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("product has been updated")

    @unittest.skipIf(not tokens, "tokens is expires")
    @unittest.skipIf(Product.objects.count() == 0, "product not have data")
    def test_product_create_add_image(self):
        urls = reverse("add-image-to-product", args=[_dat.get("public_id")])
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        data = {"image": File(open("IMG_0083.PNG", "rb")), "hex": faker.color()}
        response = self.e.post(urls, data, format="multipart")
        self.assertEqual(response.data["message"], "Image has been add to product")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("add image to product")

    @unittest.skipIf(not tokens, "tokens is expires")
    @unittest.skipIf(ProductImage.objects.count() == 0, "product not have data")
    def test_product_create_add_image(self):
        image = ProductImage.objects.first()
        urls = reverse("updated-image-to-product", args=[image.public_id])
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        data = {"image": File(open("IMG_0083.PNG", "rb")), "hex": faker.color()}
        response = self.e.post(urls, data, format="multipart")
        self.assertEqual(response.data["message"], "Image has been updated")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("updated image to product")

    @unittest.skipIf(not tokens, "tokens is expires")
    def test_product_create_code_product(self):
        urls = reverse("create-product-code")
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.get(urls, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logger.info("create product code")
