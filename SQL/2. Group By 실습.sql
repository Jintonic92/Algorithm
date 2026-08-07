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


