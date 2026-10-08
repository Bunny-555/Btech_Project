"""Run this once (python seed_data.py) to populate demo data so
segmentation, prediction and pattern mining have something to work with."""
import random
from datetime import datetime, timedelta
from app import create_app
from models import db, Customer, Product, Transaction

app = create_app()

CATEGORIES = {
    "Bakery": ["Bread", "Bun", "Cake"],
    "Dairy": ["Milk", "Butter", "Cheese", "Eggs"],
    "Grocery": ["Rice", "Oil", "Dal", "Sugar"],
    "Beverages": ["Juice", "Soda", "Coffee"],
}

with app.app_context():
    if Customer.query.count() == 0:
        for i in range(1, 51):
            db.session.add(Customer(
                name=f"Customer {i}",
                age=random.randint(18, 65),
                gender=random.choice(["Male", "Female"]),
                phone_number=f"+1-555-{random.randint(1000, 9999)}",
                location=random.choice(["Downtown", "Uptown", "Suburb", "City Center"]),
                membership_type=random.choice(["Regular", "Silver", "Gold", "Platinum"]),
            ))
        db.session.commit()

    if Product.query.count() == 0:
        pid = 1
        for cat, items in CATEGORIES.items():
            for item in items:
                db.session.add(Product(
                    product_code=f"P{100+pid}",
                    product_name=item,
                    category=cat,
                    sub_category=cat,
                    price=round(random.uniform(20, 300), 2),
                    stock=random.randint(50, 500),
                    brand="Generic",
                ))
                pid += 1
        db.session.commit()

    if Transaction.query.count() == 0:
        customers = Customer.query.all()
        products = Product.query.all()
        for t_idx in range(600):
            customer = random.choice(customers)
            product = random.choice(products)
            qty = random.randint(1, 5)
            days_ago = random.randint(0, 90)
            db.session.add(Transaction(
                transaction_code=f"T100{t_idx}",
                customer_id=customer.id,
                product_id=product.id,
                quantity=qty,
                unit_price=product.price,
                total_amount=round(product.price * qty, 2),
                transaction_date=datetime.utcnow() - timedelta(days=days_ago),
                payment_method=random.choice(["Cash", "Card", "UPI"]),
            ))
        db.session.commit()

    print("Seed data inserted successfully.")
