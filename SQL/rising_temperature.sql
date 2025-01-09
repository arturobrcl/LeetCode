# Write your MySQL query statement below
WITH PreviousWeather AS(
    SELECT id, recordDate, temperature, LAG(temperature,1) OVER (ORDER BY recordDate) AS previousTemperature
    FROM Weather
)
SELECT id FROM PreviousWeather WHERE temperature > previousTemperature;
