import stripe
from config.settings import STRIPE_API_KEY


stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product):
    """Создаем продукт в stripe."""
    title_product = f'{product.paid_course}' if product.paid_course else f'{product.paid_lesson}'
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.id


def create_stripe_price(product_id, amount_payment):
    """Создание цены в stripe."""
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount_payment * 100,
        product=product_id,
    )


def create_stripe_session(price):
    """Создание сессии на оплату в stripe."""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/success",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
