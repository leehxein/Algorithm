-- 코드를 입력하세요
SELECT ORDER_ID,PRODUCT_ID,
DATE_FORMAT(OUT_DATE, '%Y-%m-%d') as out_date,
case when out_date <= '2022-05-01' then '출고완료'
     when out_date > '2022-05-01' then '출고대기'
     else '출고미정'
end
FROM FOOD_ORDER
ORDER BY ORDER_ID