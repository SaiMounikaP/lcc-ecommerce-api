from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Numeric(scale=2))  # 2 digits after decimal point
    image_url = Column(String)


class ProductCategory(Base):
    __tablename__ = "product_categories"
    __tableargs__ = UniqueConstraint(
        "product_id", "category_id", name="uq_product_category"
    )

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey("products.id"))
    category_id = Column(ForeignKey("categories.id"))
