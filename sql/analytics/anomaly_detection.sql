WITH stats AS (

    SELECT
        AVG(credit_amount) AS avg_credit,
        STDDEV(credit_amount) AS std_credit
    FROM stg_credit
)

SELECT
    customer_id,
    credit_amount,

    ROUND(
        (
            credit_amount - avg_credit
        ) / std_credit,
        2
    ) AS z_score

FROM stg_credit
CROSS JOIN stats

WHERE ABS(
    (
        credit_amount - avg_credit
    ) / std_credit
) > 2

ORDER BY z_score DESC;