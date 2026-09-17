from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from..services import ProductService
from..schemas import ProductCreate, ProductUpdate
from..models import Product

def test_create_product():
    db = MagicMock(spec=Session)
    product_service = ProductService()
    product_create = ProductCreate(name="Product 1", price=10.0, stock=100, category="Category 1")
    product = Product(**product_create.dict())
    db.query.return_value.filter.return_value.first.return_value = None
    db.add.return_value = None
    db.commit.return_value = None
    db.refresh.return_value = None
    result = product_service.create_product(db, product_create)
    assert result.name == product_create.name

def test_get_product():
    db = MagicMock(spec=Session)
    product_service = ProductService()
    product = Product(id=1, name="Product 1", price=10.0, stock=100, category="Category 1")
    db.query.return_value.filter.return_value.first.return_value = product
    result = product_service.get_product(db, 1)
    assert result.id == product.id

def test_update_product():
    db = MagicMock(spec=Session)
    product_service = ProductService()
    product = Product(id=1, name="Product 1", price=10.0, stock=100, category="Category 1")
    product_update = ProductUpdate(name="Product 2", price=20.0, stock=200, category="Category 2")
    db.query.return_value.filter.return_value.first.return_value = product
    result = product_service.update_product(db, 1, product_update)
    assert result.name == product_update.name

def test_delete_product():
    db = MagicMock(spec=Session)
    product_service = ProductService()
    product = Product(id=1, name="Product 1", price=10.0, stock=100, category="Category 1")
    db.query.return_value.filter.return_value.first.return_value = product
    result = product_service.delete_product(db, 1)
    assert result["message"] == "Product deleted"