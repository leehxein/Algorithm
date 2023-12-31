-- 코드를 입력하세요
SELECT CCC.CAR_ID, CCC.CAR_TYPE, ROUND(DAILY_FEE * 30 * (1 - DISCOUNT_RATE * 0.01),0) AS FEE
FROM CAR_RENTAL_COMPANY_CAR CCC

JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY CCR
ON CCC.CAR_ID = CCR.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN CCD
ON CCC.CAR_TYPE = CCD.CAR_TYPE

WHERE CCC.CAR_ID NOT IN (SELECT CAR_ID
                         FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                         WHERE START_DATE < '2022-12-01' 
                         AND END_DATE > '2022-11-01') AND duration_type = '30일 이상'
GROUP BY CCC.CAR_ID
HAVING CCC.CAR_TYPE IN ('세단','SUV') AND FEE >= 500000 AND FEE<2000000

ORDER BY FEE DESC, CCC.CAR_TYPE ASC, CCC.CAR_ID DESC