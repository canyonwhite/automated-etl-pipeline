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

- Total records: TBD
- Duplicate keys: TBD
- Missing keys: TBD
- Orphaned references: TBD

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