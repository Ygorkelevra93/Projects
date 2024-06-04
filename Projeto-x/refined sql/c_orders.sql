
-- Create the table c_orders
CREATE TABLE c_orders (
    order_id        INTEGER,
    status          VARCHAR(50),
    amount          FLOAT,
    order_date      DATE,
    customer_id     INTEGER,
    cancel_date     DATE,
    products        INTEGER
);

-- Insert data into c_orders from t_orders
INSERT INTO c_orders (
    order_id,
    status,
    amount,
    order_date,
    customer_id,
    cancel_date,
    products
)
SELECT 
    CAST(order_id AS INTEGER)           AS order_id,
    status,
    CAST(amount AS FLOAT)               AS amount,
    TO_DATE(order_date, 'YYYY-MM-DD')   AS order_date,
    CAST(customer_id AS INTEGER)        AS customer_id,
    TO_DATE(cancel_date, 'YYYY-MM-DD')  AS cancel_date,
    CAST(products AS INTEGER)           AS products
FROM public.t_orders;

