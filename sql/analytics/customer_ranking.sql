SELECT
    customer_id,
    purpose,
    credit_amount,

    RANK() OVER(
        ORDER BY credit_amount DESC
    ) AS customer_rank

FROM stg_credit;