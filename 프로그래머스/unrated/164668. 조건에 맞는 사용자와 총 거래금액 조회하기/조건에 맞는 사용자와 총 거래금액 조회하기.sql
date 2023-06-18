-- 코드를 입력하세요
SELECT B.USER_ID, B.NICKNAME, sum(price) as TOTAL_SALES
from USED_GOODS_BOARD A join USED_GOODS_USER B on A.WRITER_ID = B.USER_ID
where status = 'done'
group by b.user_id
having TOTAL_SALES >= 700000
order by TOTAL_SALES asc