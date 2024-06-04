CREATE  TABLE tra_primeira_compra (
customer_id     INTEGER,
first_sale      DATE
);

INSERT INTO tra_primeira_compra (
customer_id,
first_sale
)

SELECT 
       customer_id,
       MIN(order_date) as first_sale
FROM public.c_orders
  GROUP BY  customer_id 
