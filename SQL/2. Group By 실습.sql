/************************************
   Group by 실습 - 01 
*************************************/	

USE hr_database;
SHOW tables;

-- emp 테이블에서 부서별 최대 급여, 최소 급여, 평균 급여를 구할것. 

SELECT e.deptno
	, dname
	, ROUND(MAX(sal)) as max_sal
    , ROUND(MIN(SAL)) as min_sal
    , ROUND(AVG(SAL)) as avg_sal
FROM hr_emp e
	LEFT JOIN hr_dept d ON d.deptno = e.deptno 
GROUP BY deptno
ORDER BY 1
;

-- emp 테이블에서 부서별 최대 급여, 최소 급여, 평균 급여를 구하되 평균 급여가 2000 이상인 경우만 추출. 

SELECT e.deptno
	, dname
	, ROUND(MAX(sal)) as max_sal
    , ROUND(MIN(sal)) as min_sal
    , ROUND(AVG(sal)) as avg_sal
FROM hr_emp e
	LEFT JOIN hr_dept d ON e.deptno = d.deptno
GROUP BY e.deptno
HAVING AVG(sal) >= 2000
ORDER BY 1
;

-- emp 테이블에서 부서별 최대 급여, 최소 급여, 평균 급여를 구하되 평균 급여가 2000 이상인 경우만 추출(with 절을 이용)
WITH base AS(
	SELECT deptno
		, ROUND(MAX(sal)) max_sal
        , ROUND(MIN(sal)) min_sal
        , ROUND(AVG(sal)) avg_sal
    FROM hr_emp 
    GROUP BY 1
    ORDER BY 1
)
SELECT * 
FROM base
WHERE avg_sal >= 2000
;


-- 부서명 SALES와 RESEARCH 소속 직원별로 과거부터 현재까지 모든 급여를 취합한 평균 급여


SELECT e.empno
	, e.ename
	, ROUND(AVG(h.sal)) as avg_sal
FROM hr_emp e
	LEFT JOIN hr_dept d ON e.deptno = d.deptno
	LEFT JOIN hr_emp_salary_hist h ON e.empno = h.empno
WHERE d.dname IN ('SALES', 'RESEARCH')
GROUP BY e.empno, e.ename
ORDER BY 1, 2

;


-- 부서명 SALES와 RESEARCH 소속 직원별로 과거부터 현재까지 모든 급여를 취합한 평균 급여(with 절로 풀기)


WITH base AS(
	SELECT d.dname
		, e.empno
        , e.ename
        , e.job
        , his.fromdate
        , his.todate
		, his.sal
    FROM hr_dept d
		JOIN hr_emp e ON d.deptno = e.deptno
		JOIN hr_emp_salary_hist his ON e.empno = his.empno
	WHERE d.dname IN ('SALES', 'RESEARCH')
)
SELECT empno
	, MAX(ename) AS ename
	, ROUND(AVG(sal), 2) AS avg_sal 
FROM base
GROUP BY empno 
ORDER BY 1, 2
;

/************************************
   Group by 실습 - 02(집계함수와 count(distinct))
*************************************/
-- 추가적인 테스트 테이블 생성. 
DROP TABLE IF EXISTS hr_emp_test;
CREATE TABLE hr_emp_test AS SELECT * FROM hr_emp ;
INSERT INTO hr_emp_test 
SELECT 8000, 'CHMIN', 'ANALYST', 7839, STR_TO_DATE('19810101', '%Y%m%d'), 3000, 1000, 20;
SELECT * FROM hr_emp_test;

-- Aggregation은 Null값을 처리하지 않음.


SELECT deptno
	, COUNT(*) AS cnt
    , SUM(comm)
    , MAX(comm)
    , MIN(comm)
    , AVG(comm)
FROM hr_emp_test
GROUP BY 1
;

SELECT mgr
	, COUNT(*)
    , SUM(comm)
FROM hr_emp
GROUP BY mgr
;

-- max, min 함수는 숫자열 뿐만 아니라, 문자열,날짜/시간 타입에도 적용가능. 

SELECT deptno
	, MAX(job)
    , MIN(ename)
    , MAX(hiredate)
    , MIN(hiredate)
    , SUM(ename)
    , AVG(ename)
FROM hr_emp
GROUP BY deptno
;

-- count(distinct 컬럼명)은 지정된 컬럼명으로 중복을 제거한 고유한 건수를 추출
SELECT COUNT(DISTINCT JOB) FROM hr_emp_test;

/************************************
   Group by 실습 - 03(Group by절에 가공 컬럼 및 case when 적용)
*************************************/
-- emp 테이블에서 입사년도별 평균 급여 구하기.  


SELECT YEAR(hiredate) year_
	, ROUND(AVG(sal)) as avg_sal
FROM hr_emp
GROUP BY YEAR(hiredate)
ORDER BY 1
;

-- ORACLE 
-- select to_char(hiredate, 'yyyy') as hire_year, avg(sal) as avg_sal --, count(*) as cnt
-- from hr.emp
-- group by to_char(hiredate, 'yyyy')
-- order by 1;

-- 1000미만, 1000-1999, 2000-2999와 같이 1000단위 범위내에 sal이 있는 레벨로 group by 하고 해당 건수를 구함.

 
SELECT FLOOR(sal/1000)*1000 AS bin_range
	, COUNT(*) AS cnt
FROM hr_emp
GROUP BY FLOOR(sal/1000)*1000
;

SELECT *,
	FLOOR(sal/1000)*1000 as bin_range
FROM hr_emp; 

SELECT * FROM hr_emp;
-- job이 SALESMAN인 경우와 그렇지 않은 경우만 나누어서 평균/최소/최대 급여를 구하기. 


SELECT CASE WHEN job = 'SALESMAN' THEN 'SALESMAN'
			ELSE 'OTHERS' END AS job_cat
	, ROUND(AVG(sal)) AS avg_sal
    , ROUND(MIN(sal)) AS min_sal
    , ROUND(MAX(sal)) AS max_sal
	, COUNT(*) AS cnt
FROM hr_emp 
GROUP BY 1
;


/************************************
   Group by 실습 - 04(Group by와 Aggregate 함수의 case when 을 이용한 pivoting)
*************************************/
USE hr_database;

-- deptno로 group by하고 job으로 sal을 pivoting


SELECT deptno
	, job
	, SUM(sal) as SAL
FROM hr_emp e
GROUP BY deptno, job
ORDER BY deptno
;

SELECT deptno
	, SUM(CASE WHEN job = 'SALESMAN' THEN sal END) AS sales_sum
	, SUM(CASE WHEN job = 'MANAGER' THEN sal END) AS manager_sum
    , SUM(CASE WHEN job = 'PRESIDENT' THEN sal END) AS president_sum
    , SUM(CASE WHEN job = 'ANALYST' THEN sal END) AS analyst_sum
    , SUM(CASE WHEN job = 'CLERK' THEN sal END) AS clerk_sum
    , SUM(sal) AS total_sum
FROM hr_emp 
GROUP BY deptno
ORDER BY 1
;

-- group by Pivoting시 조건에 따른 건수 계산 유형(count case when then 1 else null end)


SELECT deptno
	, COUNT(CASE WHEN job = "SALESMAN" THEN 1 END) AS sales_cnt
	, COUNT(CASE WHEN job = 'MANAGER' THEN 1 END) AS manager_cnt
    , COUNT(CASE WHEN job = "PRESIDENT" THEN 1 END) AS president_cnt
    , COUNT(CASE WHEN job = 'ANALYST' THEN 1 END) AS analyst_cnt
    , COUNT(CASE WHEN job = 'CLERK' THEN 1 END) AS clerk_cnt
    , COUNT(*) AS total_cnt
FROM hr_emp
GROUP BY deptno
ORDER BY 1
;


-- group by Pivoting시 조건에 따른 건수 계산 시 잘못된 사례(count case when then 1 else null end)


SELECT deptno
	, COUNT(CASE WHEN job = "SALESMAN" THEN 1 ELSE 0 END) AS sales_cnt
	, COUNT(CASE WHEN job = 'MANAGER' THEN 1 ELSE 0 END) AS manager_cnt
    , COUNT(CASE WHEN job = "PRESIDENT" THEN 1 ELSE NULL END) AS president_cnt
    , COUNT(CASE WHEN job = 'ANALYST' THEN 1 ELSE 0 END) AS analyst_cnt
    , COUNT(CASE WHEN job = 'CLERK' THEN 1 ELSE 0 END) AS clerk_cnt
    , COUNT(*) AS total_cnt
FROM hr_emp
GROUP BY deptno
ORDER BY 1
;

-- group by Pivoting시 조건에 따른 건수 계산 시 sum()을 이용

SELECT deptno
	, SUM(CASE WHEN job = 'SALESMAN' THEN 1 ELSE 0 END) AS sales_cnt
    , SUM(CASE WHEN job = 'MANAGER' THEN 1 ELSE 0 END) AS manager_cnt
    , SUM(CASE WHEN job = 'PRESIDENT' THEN 1 ELSE NULL END) AS president_cnt
    , SUM(CASE WHEN job = "ANALYST" THEN 1 ELSE 0 END) AS analyst_cnt
    , SUM(CASE WHEN job = 'CLERK' THEN 1 ELSE 0 END) AS clerk_cnt
FROM hr_emp
GROUP BY deptno
ORDER BY 1
;


/************************************
   Group by rollup 
*************************************/

-- deptno + job레벨 외에 dept내의 전체 job 레벨(결국 dept레벨), 전체 Aggregation 수행. 

SELECT deptno
	, job
    , SUM(sal) as sal_sum
FROM hr_emp
-- GROUP BY ROLLUP(deptno, job) << Oracle
GROUP BY deptno, job WITH ROLLUP
-- ORDER BY deptno, job
;

-- 상품 카테고리 + 상품별 매출합 구하기

SELECT c.category_name
	, p.product_name
	, SUM(amount) AS total_amt
FROM nw_order_items oi
	LEFT JOIN nw_products p ON p.product_id = oi.product_id
    LEFT JOIN nw_categories c ON p.category_id = c.category_id
GROUP BY 1, 2
ORDER BY 1, 2
;


-- 상품 카테고리 + 상품별 매출합 구하되, 상품 카테고리 별 소계 매출합 및 전체 상품의 매출합을 함께 구하기 

SELECT c.category_name
	, p.product_name
    , SUM(amount) AS total_amt
FROM nw_order_items oi
	LEFT JOIN nw_products p ON oi.product_id = p.product_id
    LEFT JOIN nw_categories c ON c.category_id = p.category_id
GROUP BY 1, 2 WITH ROLLUP
-- ORDER BY 1, 2
    ;

-- 년+월+일별 매출합 구하기
-- 월 또는 일을 01, 02와 같은 형태로 표시하려면 to_char()함수, 1, 2와 같은 숫자값으로 표시하려면 date_part()함수 사용.

SHOW TABLES;
SELECT * FROM nw_orders;
SELECT * FROM nw_order_items;

SELECT YEAR(o.order_date) AS year_
	, MONTH(o.order_date) AS month_
    , DAY(o.order_date) AS day_
    , SUM(oi.amount) AS amt_sum
FROM nw_order_items oi
	LEFT JOIN nw_orders o ON oi.order_id = o.order_id
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3
;

-- 년+월+일별 매출합 구하되, 월별 소계 매출합, 년별 매출합, 전체 매출합을 함께 구하기

WITH base AS (
SELECT DATE_FORMAT(o.order_date, '%Y') AS year_
	, DATE_FORMAT(o.order_date, '%m') AS month_
    , DATE_FORMAT(o.order_date, '%d') AS day_
    , SUM(oi.amount) AS amt_sum
FROM nw_order_items oi
	LEFT JOIN nw_orders o ON oi.order_id = o.order_id
GROUP BY 1, 2, 3 WITH ROLLUP
-- ORDER BY 1, 2, 3
)
SELECT CASE WHEN year_ IS NULL THEN '총매출' ELSE year_ END AS year_
	, CASE WHEN year_ IS NULL THEN NULL 
		ELSE CASE WHEN month_ IS NULL THEN '년 총매출' ELSE month_ END
	  END AS month_
	, CASE WHEN year_ IS NULL OR month_ IS NULL THEN NULL
		ELSE CASE WHEN day_ IS NULL THEN '월 총매출' ELSE day_ END
	  END AS day_
	, amt_sum
FROM base
ORDER BY 1, 2, 3

;


/************************************
   Group by cube
*************************************/



-- deptno, job의 가능한 결합으로 Group by 수행. 
SELECT deptno
	, job
    , SUM(sal) AS sal_sum
FROM hr_emp
GROUP BY CUBE(deptno, job) -- << ORACLE 
ORDER BY 1, 2
;

SELECT deptno
     , job
     , sal_sum
FROM (
    -- 1. (deptno, job), (deptno), () 조합
    SELECT deptno, job, SUM(sal) AS sal_sum
    FROM hr_emp
    GROUP BY deptno, job WITH ROLLUP

    UNION ALL

    -- 2. (job) 단독 조합 (전체 직무별 소계)
    SELECT NULL AS deptno, job, SUM(sal) AS sal_sum
    FROM hr_emp
    WHERE job IS NOT NULL
    GROUP BY job
) t
ORDER BY 
	deptno IS NULL,
--     CASE WHEN deptno IS NULL THEN 1 ELSE 0 END,  -- deptno가 NULL이면 뒤로(1)
    deptno ASC,                                      -- deptno 오름차순
    CASE WHEN job IS NULL THEN 1 ELSE 0 END,     -- job이 NULL이면 뒤로(1)
    job ASC		                                   -- job 오름차순
;


-- 상품 카테고리 + 상품별 + 주문처리직원별 매출

SELECT c.category_name
	, p.product_name
    , CONCAT(e.last_name, ' ', e.first_name) AS employee_name
    , SUM(amount) AS amt_sum
FROM nw_order_items oi 
	LEFT JOIN nw_orders o ON o.order_id = oi.order_id
    LEFT JOIN nw_products p ON p.product_id = oi.product_id
    LEFT JOIN nw_categories c ON c.category_id = p.category_id
    LEFT JOIn nw_employees e ON e.employee_id = o.employee_id
GROUP BY c.category_name, p.product_name, e.employee_id
ORDER BY 1, 2, 3
;

-- 상품 카테고리, 상품별, 주문처리직원별 가능한 결합으로 Group by 수행

SELECT category_name
     , product_name
     , emp_name
     , SUM(amount) AS sum_amount
FROM (
    -- 1. (category_name, product_name, emp_name), (category_name, product_name), (category_name), ()
    SELECT c.category_name
         , b.product_name
         , CONCAT(e.last_name, e.first_name) AS emp_name
         , a.amount
    FROM nw_order_items a
        JOIN nw_products b ON a.product_id = b.product_id
        JOIN nw_categories c ON b.category_id = c.category_id
        JOIN nw_orders d ON a.order_id = d.order_id
        JOIN nw_employees e ON d.employee_id = e.employee_id
) t
GROUP BY category_name, product_name, emp_name WITH ROLLUP

UNION ALL

-- 2. (category_name, emp_name) 조합
SELECT c.category_name
     , NULL AS product_name
     , CONCAT(e.last_name, e.first_name) AS emp_name
     , SUM(a.amount) AS sum_amount
FROM nw_order_items a
    JOIN nw_products b ON a.product_id = b.product_id
    JOIN nw_categories c ON b.category_id = c.category_id
    JOIN nw_orders d ON a.order_id = d.order_id
    JOIN nw_employees e ON d.employee_id = e.employee_id
WHERE e.last_name IS NOT NULL AND e.first_name IS NOT NULL
GROUP BY c.category_name, CONCAT(e.last_name, e.first_name)

UNION ALL

-- 3. (product_name, emp_name) 및 (emp_name) 조합
SELECT NULL AS category_name
     , b.product_name
     , CONCAT(e.last_name, e.first_name) AS emp_name
     , SUM(a.amount) AS sum_amount
FROM nw_order_items a
    JOIN nw_products b ON a.product_id = b.product_id
    JOIN nw_categories c ON b.category_id = c.category_id
    JOIN nw_orders d ON a.order_id = d.order_id
    JOIN nw_employees e ON d.employee_id = e.employee_id
WHERE e.last_name IS NOT NULL AND e.first_name IS NOT NULL
GROUP BY b.product_name, CONCAT(e.last_name, e.first_name) WITH ROLLUP

UNION ALL

-- 4. (product_name) 단독 소계 조합
SELECT NULL AS category_name
     , b.product_name
     , NULL AS emp_name
     , SUM(a.amount) AS sum_amount
FROM nw_order_items a
    JOIN nw_products b ON a.product_id = b.product_id
    JOIN nw_categories c ON b.category_id = c.category_id
    JOIN nw_orders d ON a.order_id = d.order_id
    JOIN nw_employees e ON d.employee_id = e.employee_id
WHERE b.product_name IS NOT NULL
GROUP BY b.product_name

ORDER BY 
    CASE WHEN category_name IS NULL THEN 1 ELSE 0 END ASC,
    category_name ASC,
    CASE WHEN product_name IS NULL THEN 1 ELSE 0 END ASC,
    product_name ASC,
    CASE WHEN emp_name IS NULL THEN 1 ELSE 0 END ASC,
    emp_name ASC
;


