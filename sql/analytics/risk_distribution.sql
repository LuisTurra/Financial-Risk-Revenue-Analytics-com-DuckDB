SELECT
    CASE
        WHEN risk = 2 THEN 'bad'
        ELSE 'good'
    END AS risk_label,

    COUNT(*) AS total_clients,

    ROUND(
        COUNT(*) * 100.0 /
        SUM(COUNT(*)) OVER(),
        2
    ) AS percentage

FROM stg_credit

GROUP BY risk;