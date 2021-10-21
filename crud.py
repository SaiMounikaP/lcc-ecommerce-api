from sqlalchemy import and_, select

from models import Category, Product, ProductCategory


def get_categories(db_session):
    return db_session.execute(select(Category)).scalars().all()


def get_category_by_id(db_session, category_id):
    return db_session.get(Category, category_id)


def get_products_by_category(db_session, category_id):
    statement = select(Product).join_from(
        Product,
        ProductCategory,
        and_(
            ProductCategory.category_id == category_id,
            ProductCategory.product_id == Product.id,
        ),
    )

    return db_session.execute(statement).scalars().all()


def get_products(db_session):
    return db_session.execute(select(Product)).scalars().all()


def get_product_by_id(db_session, product_id):
    return db_session.get(Product, product_id)
