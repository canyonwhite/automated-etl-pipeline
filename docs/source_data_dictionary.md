# Olist Source Data Dictionary

## Dataset: Orders

**Source File:** olist_orders_dataset.csv

**Expected Grain:** One row per order

**Proposed Primary Key:** order_id

### Columns

| Column | Data Type | Nullable | Description |
|--------|-----------|----------|-------------|
| order_id | String | TBD | Unique order identifier |
| customer_id | String | TBD | Reference to customer |
| order_status | String | TBD | Order status |

### Relationships

- orders.customer_id -> customers.customer_id

### Data Quality Findings

- Total records: 99441
- Duplicate keys: 0
- Missing keys: 0
- Orphaned references: 0

## Dataset: Order_Items

**Source File:** olist_order_items_dataset.csv

**Expected Grain:** One row per (order_item_id, order_id)

**Proposed Primary Key:** order_item_id

### Columns

| Column | Data Type | Nullable | Description |
|--------|-----------|----------|-------------|
| order_id | object | TBD | Unique order identifier |
| order_item_id | int64 | TBD | Unique order item identifier |
| product_id | object | TBD | Reference to product |
| seller_id | object | TBD | Reference to seller |
| shipping_limit-date | object | TBD | NA |
| price | float64 | TBD | Price of item |
| freight_value | float64 | Price of shipping |

### Relationships

- order_items.order_id -> orders.order_id
- order_items.product_id -> products.product_id
- order_items.seller_id -> sellers.seller_id

### Data Quality Findings

- Total records: 112650
- Duplicate keys: 0
- Missing keys: 0
- Orphaned references: 0

## Dataset: Payments

**Source File:** olist_order_payments_dataset.csv

**Expected Grain:** One row per (order_id, payment_sequential)

**Proposed Primary Key:** payment_sequential

### Columns

| Column | Data Type | Nullable | Description |
|--------|-----------|----------|-------------|
| order_id | object | TBD | Unique order identifier |
| payment_sequential | int64 | TBD | Unique payment identifier |
| payment_type | object | TBD | Unique payment type |
| payment_installments | int64 | TBD | Number of payments to be made |
| payment_value | float64 | TBD | Total value of payment |

### Relationships

- payments.order_id -> orders.order_id

### Data Quality Findings

- Total records: 103886
- Duplicate keys: 0
- Missing keys: 0
- Orphaned references: 0

## Dataset: Customers

**Source File:** olist_customers_dataset.csv

**Expected Grain:** One row per customer

**Proposed Primary Key:** customer_id

### Columns

| Column | Data Type | Nullable | Description |
|--------|-----------|----------|-------------|
| customer_id | object | TBD | Customer identifier |
| customer_unique_id | object | TBD | Unique customer identifier |
| customer_zip_code_prefix | String | TBD | Zip code per customer |
| customer_city | object | TBD | City customer is located in |
| customer_state | object | TBD | State customer is located in |

### Relationships

- orders.customer_id -> customers.customer_id

### Data Quality Findings

- Total records: 99441
- Duplicate keys: 0
- Missing keys: 0
- Orphaned references: 0