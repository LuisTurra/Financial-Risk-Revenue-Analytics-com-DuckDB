SELECT
    purpose,

    COUNT(*) AS total_loans,

    ROUND(
        AVG(credit_amount),
        2
    ) AS avg_loan_amount,

    SUM(credit_amount) AS total_credit_volume

FROM stg_credit

GROUP BY purpose

ORDER BY total_credit_volume DESC;