SELECT
    COUNT(*) AS total_clients,

    SUM(credit_amount) AS total_credit_volume,

    ROUND(
        AVG(credit_amount),
        2
    ) AS avg_credit,

    ROUND(
        AVG(duration),
        2
    ) AS avg_duration,

    COUNT(
        CASE
            WHEN risk = 2
            THEN 1
        END
    ) AS risky_clients

FROM stg_credit;