SELECT
    customer_id,
    credit_amount,

    SUM(credit_amount) OVER(
        ORDER BY customer_id
        ROWS BETWEEN 9 PRECEDING AND CURRENT ROW
    ) AS rolling_credit_10_clients

FROM stg_credit;