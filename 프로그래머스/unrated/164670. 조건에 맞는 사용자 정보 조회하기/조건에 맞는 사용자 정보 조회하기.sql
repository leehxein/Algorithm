-- 코드를 입력하세요
SELECT uu.USER_ID,
uu.NICKNAME,
concat(city, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as '전체주소',
CONCAT_WS("-", SUBSTRING(uu.TLNO, 1, 3), SUBSTR(uu.TLNO, 4, 4), RIGHT(uu.TLNO, 4)) AS "전화번호"
from USED_GOODS_BOARD ub join USED_GOODS_USER uu on ub.WRITER_ID = uu.USER_ID
group by ub.WRITER_ID
having count(ub.WRITER_ID) >= 3
order by uu.USER_ID desc