CREATE TABLE c_customers (
    customer_id     INTEGER,
    name            VARCHAR(255),
    email           VARCHAR(255),
    country         VARCHAR(255),
    lead_id         INTEGER,
    orders          VARCHAR(50)
);

INSERT INTO c_customers (
customer_id,
       name,
       email,
       country,
       lead_id,
       orders
       
       )
SELECT CAST(customer_id as NUMERIC)  as  customer_id,
       name,
       email,
       country,
       CAST(lead_id AS NUMERIC) as lead_id,
       orders
FROM public.t_customers


