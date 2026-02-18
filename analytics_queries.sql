-- Turnover Rate by Department
SELECT 
    Department,
    COUNT(*) AS Headcount,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS AttritionCount,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS TurnoverRate
FROM Employees
GROUP BY Department
ORDER BY TurnoverRate DESC;

-- Diversity Metrics
SELECT 
    Gender,
    COUNT(*) AS Count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM Employees), 2) AS Percentage,
    AVG(MonthlyIncome) AS AvgIncome
FROM Employees
GROUP BY Gender;

-- High-Risk Employees (Low Satisfaction + High Distance)
SELECT EmpID, JobRole, Department, Attrition
FROM Employees
WHERE JobSatisfaction <= 2 AND DistanceFromHome > 15;
