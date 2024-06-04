CREATE TABLE c_leads (
    lead_id     INTEGER,
    lead_date   DATE,
    name        VARCHAR(255),
    email       VARCHAR(255),
    status      VARCHAR(50),
    origin      VARCHAR(50)
);

INSERT INTO c_leads (lead_id, lead_date, name, email, status, origin)
SELECT 
    CAST(lead_id AS NUMERIC)            AS lead_id,
    TO_DATE(lead_date, 'YYYY-MM-DD'  )  AS lead_date,
    name,
    email,
    status,
    origin
FROM public.t_leads;
