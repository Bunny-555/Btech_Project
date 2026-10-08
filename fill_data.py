import random
from datetime import datetime, timedelta
from app import app
from models import db, Customer, Product, Transaction
import uuid

def generate_mock_transactions(num_transactions=200):
    with app.app_context():
        customers = Customer.query.all()
        products = Product.query.all()

        if not customers or not products:
            print("Need at least 1 customer and 1 product to generate transactions.")
            return

        print(f"Generating {num_transactions} mock transactions...")
        
        # We will generate transactions over the last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        for _ in range(num_transactions):
            customer = random.choice(customers)
            product = random.choice(products)
            
            # Random date within the last 30 days
            random_days = random.randint(0, 30)
            random_hours = random.randint(0, 23)
            random_minutes = random.randint(0, 59)
            
            txn_date = start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)
            
            quantity = random.randint(1, 5)
            total_amount = product.price * quantity
            
            txn = Transaction(
                transaction_code=str(uuid.uuid4())[:8].upper(),
                customer_id=customer.id,
                product_id=product.id,
                quantity=quantity,
                unit_price=product.price,
                total_amount=total_amount,
                transaction_date=txn_date,
                payment_method=random.choice(['Cash', 'Credit Card', 'UPI'])
            )
            db.session.add(txn)
            
        db.session.commit()
        print("Mock transactions generated successfully!")

if __name__ == "__main__":
    generate_mock_transactions(500)
