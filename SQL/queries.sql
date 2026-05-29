SELECT
    ds AS date,
    yhat AS predicted_value,
    yhat_lower,
    yhat_upper
FROM `your_project.forecast_dataset.forecast_table`
ORDER BY date;
