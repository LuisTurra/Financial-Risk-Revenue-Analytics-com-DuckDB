SELECT
    sex,
    housing,
    purpose,

    COUNT(*) AS total_clients,

    ROUND(
        AVG(credit_amount),
        2
    ) AS avg_credit,

    SUM(credit_amount) AS total_credit_volume

FROM stg_credit

GROUP BY
    sex,
    housing,
    purpose

ORDER BY total_credit_volume DESC;