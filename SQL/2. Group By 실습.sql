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

