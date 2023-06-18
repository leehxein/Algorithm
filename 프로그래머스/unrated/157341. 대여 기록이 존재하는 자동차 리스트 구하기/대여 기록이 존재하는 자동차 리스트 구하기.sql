-- 코드를 입력하세요
SELECT a.CAR_ID
from CAR_RENTAL_COMPANY_CAR A join CAR_RENTAL_COMPANY_RENTAL_HISTORY B
on a.CAR_ID = b.CAR_ID
where a.CAR_TYPE = '세단' and START_DATE like '2022-10%'
group by a.car_id
order by a.car_id desc