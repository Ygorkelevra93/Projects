SELECT 
    LEAD.lead_id                            AS "CODIGO_LEAD",
    TO_CHAR(LEAD.lead_date, 'MM/YYYY')      AS "DATA REF CADASTRO_LEAD",
    TO_CHAR(LEAD.lead_date, 'DD/MM/YYYY')   AS "DATA_CADASTRO_LEAD",
    LEAD.name                               AS "NOME_LEAD",
    LEAD.email                              AS "EMAIL_LEAD",
    LEAD.status                             AS "STATUS_LEAD",
    LEAD.origin                             AS "CANAL_RECEBIMENTO_LEAD",
    -- customers 
    CUST.customer_id                        AS "CODIGO_CLIENTE",
    CUST.country                            AS "PAIS",
    CUST.lead_id                            AS "CODIGO_LEAD_CLIENTE",
    -- orders 
    ORDE.customer_id                        AS "CODIGO_CLIENTE_COMPRA",
    ORDE.order_id                           AS "NOTA_FISCAL",
    ORDE.status                             AS "STATUS_VENDA",
    TO_CHAR(ORDE.order_date, 'DD/MM/YYYY')  AS "DATA_VENDA",
    TO_CHAR(ORDE.cancel_date, 'DD/MM/YYYY') AS "DATA_CANCELAMENTO",
    TO_CHAR(ORDE.cancel_date, 'MM/YYYY')    AS "DATA_REF_CANCELAMENTO",
    -- ORDE.products,
    ORDE.amount                             AS "VALOR_NOTA",
    -- products 
    PROD.product_id                         AS "CODIGO_PRODUTO",
    PROD.product_name                       AS "NOME_PRODUTO",
    PROD.product_price                      AS "VALOR_UNITARIO",
    PROD.category                           AS "CATEGORIA_PRODUTO",
    PROD.segment                            AS "SEGMENTO_PRODUTO",
    CONVER.conversao                        AS "CONVERSAO"
FROM public.c_leads              AS LEAD
LEFT JOIN public.c_customers     AS CUST ON CUST.lead_id = LEAD.lead_id
LEFT JOIN public.c_orders        AS ORDE ON ORDE.customer_id = CUST.customer_id
LEFT JOIN public.c_products      AS PROD ON PROD.product_id = ORDE.products
LEFT JOIN (
    SELECT 
        PRI.customer_id,
        PRI.first_sale,
        LEAD.lead_date,
        (PRI.first_sale - LEAD.lead_date)   AS conversao

    FROM public.tra_primeira_compra                 AS PRI
    LEFT JOIN public.c_leads                        AS LEAD ON LEAD.lead_id = PRI.customer_id
)                       AS CONVER ON CONVER.customer_id = ORDE.customer_id;
