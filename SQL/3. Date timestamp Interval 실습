/************************************
일별 세션건수, 일별 방문 사용자(유저), 사용자별 평균 세션 수
*************************************/
USE second_database;


WITH base AS(
	SELECT DATE_FORMAT(DATE(visit_stime), '%Y-%m-%d') AS d_day
    , COUNT(DISTINCT sess_id) AS daily_sess_cnt
    , COUNT(sess_id) AS daily_sess_cnt_again
    , COUNt(DISTINCT user_id) AS daily_user_cnt
    FROM ga_sessions
)
SELECT *
	, 1.0 * daily_sess_cnt / daily_user_cnt AS avg_user_sessions
FROM base
;

/************************************
DAU, WAU, MAU 구하기
*************************************/
/* 아래는 이미 많은 과거 데이터가 있을 경우를 가정하고 DAU, WAU, MAU를 추출함 */

-- 일별 방문한 고객 수(DAU) --------------------------------------------------------------

SELECT DATE(visit_stime) AS d_day
	, COUNT(DISTINCT user_id) AS user_cnt
FROM ga_sessions
-- WHERE visit_stime BETWEEN STR_TO_DATE('2016-10-25', '%Y-%m-%d') AND STR_TO_DATE('2026-10-31 23:59:59', '%Y-%m-%d %H:%i:%s')
GROUP BY 1
ORDER BY 1
;

-- 주별 방문한 고객수(WAU) --------------------------------------------------------------


SELECT STR_TO_DATE(DATE_FORMAT(visit_stime, '%x-%v-1'), '%x-%v-%w') AS week_day
-- %연도 %주차번호 %요일번호 (월요일 1)
-- %연도 %주차번호 %표준 요일 번호 (월요일의 날짜 2 > 9 > ... )
	, COUNT(DISTINCT user_id) AS user_cnt
FROM ga_sessions
GROUP BY 1
ORDER BY 1
;


-- 월별 방문한 고객수(MAU) --------------------------------------------------------------

SELECT DATE_FORMAT(visit_stime, '%Y-%m-01') AS ym
	, COUNT(DISTINCT user_id) AS user_cnt
FROM ga_sessions 
GROUP BY 1
ORDER BY 1
;

-- interval로 전일 7일 구하기 --------------------------------------------------------------

SELECT DATE_FORMAT(visit_stime, '%Y-%m-%d') AS d_day
	, STR_TO_DATE(visit_stime, '%Y-%m-%d') - INTERVAL 7 DAY as 7days_b4
FROM ga_sessions
GROUP BY 1
;

-- 오늘을 기준으로 전 7일의 WAU 구하기


SELECT * 
FROM ga_sessions
WHERE d_day BETWEEN DATE_SUB(CURRENT_DATE() , INTERVAL 7 DAY) AND curr_date
;



;
