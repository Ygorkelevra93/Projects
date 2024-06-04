SELECT customer_id,
       first_sale,
       lead_date,
       first_sale - lead_date   as conversao
FROM public.tra_primeira_compra as PRI

LEFT JOIN (
SELECT lead_id,
       lead_date
FROM public.c_leads) AS LEAD on lead.lead_id = PRI.customer_id 