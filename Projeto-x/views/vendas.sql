SELECT 
    TO_CHAR(ORDE.order_date, 'MM/YYYY')     AS "DATA REF",
    TO_CHAR(ORDE.order_date, 'DD/MM/YYYY')  AS "DATA VENDA",
    ORDE.order_id                           AS "NOTA FISCAL",
    ORDE.status                             AS "STATUS",
    ORDE.amount                             AS "VALOR NOTA FISCAL",
    TO_CHAR(ORDE.order_date, 'DD/MM/YYYY')  AS "DATA VENDA",
    ORDE.customer_id                        AS "CODIGO CLIENTE",
    TO_CHAR(ORDE.cancel_date, 'DD/MM/YYYY') AS "DATA CANCELAMENTO",
    COUNT(ORDE.products)                    AS "QUANTIDADE",
    CUST.country                            AS "PAÍS"
FROM 
    public.c_orders AS ORDE
LEFT JOIN
    public.c_customers AS CUST ON ORDE.customer_id = CUST.customer_id
GROUP BY 
    TO_CHAR(ORDE.order_date, 'MM/YYYY'), 
    ORDE.order_id,
    ORDE.status,
    ORDE.amount,
    ORDE.order_date,
    ORDE.customer_id,
    ORDE.cancel_date,
    CUST.country;