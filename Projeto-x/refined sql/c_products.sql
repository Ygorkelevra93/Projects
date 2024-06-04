CREATE TABLE c_products (
    product_id      INTEGER,
    product_name    VARCHAR(255),
    product_price   FLOAT,
    category        VARCHAR(100),
    segment         VARCHAR(80)
);

INSERT INTO c_products (
    product_id,
    product_name,
    product_price,
    category,
    segment
)
SELECT 
    CAST(product_id AS NUMERIC)     AS product_id,
    name AS product_name,
    CAST(price AS FLOAT)            AS product_price,
    category,
    segment
FROM public.t_products;
