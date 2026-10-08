# Supermarket Customer Behavior Analysis & Predictive Modeling

Flask web app implementing customer/product/transaction management, K-Means
segmentation, SVM & MLP purchase prediction, and sequential pattern mining.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create the DB and (optionally) seed demo data
python -c "from app import create_app; create_app()"
python seed_data.py           # optional: populates demo customers/products/transactions

python app.py
```

Visit http://127.0.0.1:5000, register an account, then log in.

## Flow
1. Register/Login
2. Add Customers & Products (or use `seed_data.py` for demo data)
3. Add Transactions (manually or upload CSV with columns: customer_id, product_id, quantity, unit_price)
4. Analytics -> Segmentation runs K-Means on RFM features
5. Prediction -> Train Models, then predict purchase likelihood via SVM/MLP
6. Patterns -> View frequent sequential purchase patterns
