MODEL (
    name bronze.stg_orders_olist,
    kind VIEW,
    description "one row per order"
);

SELECT
    orders.ORDER_ID AS order_id,
    orders.CUSTOMER_ID AS customer_id,
    orders.ORDER_STATUS AS order_status,
    TRY_TO_TIMESTAMP_NTZ(
        orders.ORDER_PURCHASE_TIMESTAMP
    ) AS purchased_at,
    CAST(purchased_at AS DATE) AS purchase_date
FROM RETAIL_DB.RAW.ORDERS AS orders