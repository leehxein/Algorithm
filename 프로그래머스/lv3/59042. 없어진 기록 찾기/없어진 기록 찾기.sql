-- 코드를 입력하세요
SELECT ao.animal_id as ANIMAL_ID, ao.name as NAME
from ANIMAL_INS ai right join ANIMAL_OUTS ao on ai.ANIMAL_ID = ao.ANIMAL_ID
where ai.animal_id is null
order by ao.animal_id