************************************
   조인 실습 - 1
*************************************/

USE hr_database;
SHOW tables;
-- 직원 정보와 직원이 속한 부서명 가져오기
SELECT e.*, d.dname
FROM hr_emp e
	JOIN hr_dept d on e.deptno = d.deptno 
;

-- Job이 salesman인 직원정보와 직원이 속한 부서명 가져오기

SELECT e.*, d.dname
FROM hr_emp e
	JOIN hr_dept d on e.deptno = d.deptno 
WHERE e.job = 'SALESMAN'
;

-- 부서명 SALES와 RESEARCH의 소속 직원들의 부서명, 직원번호, 직원명, JOB 그리고 과거 급여 정보 추출 

SELECT a.dname, b.empno, b.ename, b.job, c.fromdate, c.todate, c.sal 
FROM hr_dept a
	JOIN hr_emp b ON a.deptno = b.deptno
	JOIN hr_emp_salary_hist c ON b.empno = c.empno
WHERE a.dname IN ('SALES', 'RESEARCH')
ORDER BY a.dname, b.empno, c.fromdate
;

-- 부서명 SALES와 RESEARCH의 소속 직원들의 부서명, 직원번호, 직원명, JOB 그리고 과거 급여 정보중 1983년 이전 데이터는 무시하고 데이터 추출 
SELECT d.dname, e.empno, e.ename, e.job, h.fromdate, h.todate, h.sal
FROM hr_emp e
	JOIN hr_dept d ON e.deptno = d.deptno
    JOIN hr_emp_salary_hist h ON e.empno = h.empno
WHERE d.dname IN ('SALES', 'RESEARCH')
	AND YEAR(h.fromdate) >= 1983
-- AND h.fromdate >= '19830101'
-- AND h.fromdate >= STR_TO_DATE('19830101', '%Y%m%d')
-- ORACLE : AND h.fromdate >= TO_DATE('19830101', 'YYYYMMDD')
ORDER BY 1, 2, h.fromdate
;

-- 부서명 SALES와 RESEARCH 소속 직원별로 과거부터 현재까지 모든 급여를 취합한 평균 급여

SELECT dname, e.empno, e.ename, round(AVG(h.sal), 0) as average
FROM hr_emp e 
	JOIN hr_dept d on e.deptno = d.deptno
    JOIN hr_emp_salary_hist h on e.empno = h.empno
WHERE d.dname in ('SALES', 'RESEARCH')
GROUP BY 1, 2, 3 
ORDER BY 1, 2, 3
;

-- 직원명 SMITH의 과거 소속 부서 정보
SELECT d.dname, h.fromdate, h.todate
FROM hr_emp_salary_hist h
    JOIN hr_emp e on h.empno = e.empno 
	JOIN hr_dept d on d.deptno = e.deptno
WHERE e.ename = 'SMITH'
;
