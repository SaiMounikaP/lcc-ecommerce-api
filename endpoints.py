from flask import Blueprint, abort, jsonify

import crud
from db import SessionLocal

bp = Blueprint("endpoints", __name__, url_prefix="/")


@bp.get("/categories")
def read_categories():
    db_session = SessionLocal()
    categories = crud.get_categories(db_session)
    db_session.close()

    categories_json = [{"id": item.id, "name": item.name} for item in categories]

    return jsonify(categories_json)


@bp.get("/categories/<int:category_id>")
def read_products_by_category(category_id):
    db_session = SessionLocal()
    category = crud.get_category_by_id(db_session, category_id)

    if not category:
        abort(404, description="The category with the category ID does not exist")

    products = crud.get_products_by_category(db_session, category_id)
    db_session.close()

    products_json = [
        {
            "id": item.id,
            "title": item.title,
            "price": item.price,
            "image_url": item.image_url,
        }
        for item in products
    ]

    response_json = {
        "id": category_id,
        "name": category.name,
        "products": products_json,
    }

    return jsonify(response_json)


@bp.get("/products")
def read_products():
    db_session = SessionLocal()
    products = crud.get_products(db_session)
    db_session.close()

    products_json = [
        {
            "id": item.id,
            "title": item.title,
            "price": item.price,
            "image_url": item.image_url,
        }
        for item in products
    ]

    return jsonify(products_json)


@bp.get("/products/<int:product_id>")
def read_product_by_id(product_id):
    db_session = SessionLocal()
    product = crud.get_product_by_id(db_session, product_id)
    db_session.close()

    if not product:
        abort(404, description="The product with the product ID does not exist")

    product_json = {
        "id": product.id,
        "title": product.title,
        "description": product.description,
        "price": product.price,
        "image_url": product.image_url,
    }

    return jsonify(product_json)
