CREATE OR REPLACE VIEW stg_credit AS

SELECT
    ROW_NUMBER() OVER() AS customer_id,
    age,
    sex,
    job,
    housing,
    saving_accounts,
    checking_account,
    credit_amount,
    duration,
    purpose,
    risk
FROM credit_data;