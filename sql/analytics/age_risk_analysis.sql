WITH age_groups AS (

    SELECT

        CASE
            WHEN age < 25 THEN '18-24'
            WHEN age BETWEEN 25 AND 34 THEN '25-34'
            WHEN age BETWEEN 35 AND 49 THEN '35-49'
            ELSE '50+'
        END AS age_group,

        CASE
            WHEN risk = 2 THEN 'bad'
            ELSE 'good'
        END AS risk_label

    FROM stg_credit
)

SELECT
    age_group,
    risk_label,
    COUNT(*) AS total_clients

FROM age_groups

GROUP BY
    age_group,
    risk_label

ORDER BY age_group;