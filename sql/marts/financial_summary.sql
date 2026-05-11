CREATE OR REPLACE TABLE financial_summary AS

SELECT
    purpose,
    housing,

    COUNT(*) AS total_clients,

    SUM(credit_amount) AS total_credit_volume,

    ROUND(
        AVG(credit_amount),
        2
    ) AS avg_credit_amount,

    COUNT(
        CASE
            WHEN risk = 2
            THEN 1
        END
    ) AS risky_clients

FROM stg_credit

GROUP BY
    purpose,
    housing;