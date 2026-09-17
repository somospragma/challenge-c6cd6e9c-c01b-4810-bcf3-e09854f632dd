from sqlalchemy.orm import Session
from..models import Product
from..schemas import ProductCreate, ProductUpdate, ProductResponse

class ProductService:
    def create_product(self, db: Session, product: ProductCreate):
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return ProductResponse.from_orm(db_product)

    def get_product(self, db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return ProductResponse.from_orm(product)

    def update_product(self, db: Session, product_id: int, product: ProductUpdate):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return ProductResponse.from_orm(db_product)

    def delete_product(self, db: Session, product_id: int):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted"}