/************************************
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

SELECT * FROM hr_emp;
SELECT * FROM hr_dept;
SELECT * FROM hr_emp_salary_hist;
SELECT * FROM hr_emp_dept_hist;

/************************************
   조인 실습 - 2
*************************************/
USE hr_database;
SHOW tables;

-- 고객명 Antonio Moreno이 1997년에 주문한 주문 정보를 주문 아이디, 주문일자, 배송일자, 배송 주소를 고객 주소와 함께 구할것.  

SELECT c.contact_name
	, c.address 
    , o.order_id
	, o.order_date
    , o.shipped_date
	, o.ship_address
FROM nw_customers c
	JOIN nw_orders o on c.customer_id = o.customer_id
WHERE c.contact_name = 'Antonio Moreno'
	AND YEAR(o.order_date) = 1997
-- ORACLE :: and o.order_date between to_date('19970101', 'yyyymmdd') and to_date('19971231', 'yyyymmdd')
;

-- Berlin에 살고 있는 고객의 고객명, 주문id, 주문일자, 주문접수 직원명, 배송업체명을 구할것. 

SELECT c.contact_name
	, o.order_id
    , o.order_date
    , CONCAT(first_name, ' ', last_name) as employee_name
    , s.company_name as shipper_name
FROM nw_customers c
	JOIN nw_orders o ON o.customer_id = c.customer_id
    JOIN nw_shippers s ON o.ship_via = s.shipper_id
    JOIN nw_employees e ON o.employee_id = e.employee_id
WHERE c.city rlike 'Berlin'
ORDER BY 2
;

-- Beverages 카테고리에 속하는 모든 상품아이디와 상품명, 그리고 이들 상품을 제공하는 supplier 회사명 정보 구할것 

SELECT p.product_id
	, p.product_name
    , s.company_name as supplier_name
FROM nw_products p
	JOIN nw_categories c on p.category_id = c.category_id
    JOIN nw_suppliers s on p.supplier_id = s.supplier_id
WHERE c.category_name = 'Beverages'
;

-- 고객명 Antonio Moreno이 1997년에 주문한 주문 상품정보를 고객 주소, 주문 아이디, 주문일자, 배송일자, 배송 주소 및
-- 주문 상품아이디, 주문 상품명, 주문 상품별 금액, 주문 상품이 속한 카테고리명, supplier명을 구할 것. 

SELECT c.address
	, o.order_id
    , o.order_date
    , o.shipped_date
    , o.ship_address
    , p.product_id
    , p.product_name
    , oi.amount
    , cat.category_name
    , s.contact_name as supplier_name
FROM nw_customers c
	JOIN nw_orders o ON c.customer_id = o.customer_id
    JOIN nw_order_items oi ON oi.order_id = o.order_id
    JOIN nw_products p ON p.product_id = oi.product_id
    JOIN nw_categories cat ON cat.category_id = p.category_id 
    JOIN nw_suppliers s ON s.supplier_id = p.supplier_id
WHERE c.contact_name = 'Antonio Moreno' 
	AND YEAR(o.order_date) = 1997
;

/************************************
   조인 실습 - Outer 조인. 
*************************************/	
USE hr_database;

-- 주문이 단 한번도 없는 고객 정보 구하기.
 
SELECT DISTINCT c.customer_id	
	, c.company_name
    , c.contact_name
    , c.contact_title
    , c.address
    , c.city
    , c.country
    , c.phone
    , c.fax
FROM nw_customers c
	LEFT JOIN nw_orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
;
 
select *
from nw_customers a
	left join nw_orders b on a.customer_id = b.customer_id
where b.customer_id is null;

-- 부서정보와 부서에 소속된 직원명 정보 구하기. 부서가 직원을 가지고 있지 않더라도 부서정보는 표시되어야 함. 
-- hr_table 활용 
USE hr_database;
SHOW tables;

SELECT d.*
	, e.empno
	, e.ename
    , e.job
FROM hr_dept d
	LEFT JOIN hr_emp e ON d.deptno = e.deptno
;

SELECT * FROM hr_dept;
SELECT * FROM hr_emp;

-- Madrid에 살고 있는 고객이 주문한 주문 정보를 구할것.
-- 고객명, 주문id, 주문일자, 주문접수 직원명, 배송업체명을 구하되, 
-- 만일 고객이 주문을 한번도 하지 않은 경우라도 고객정보는 빠지면 안됨.
-- 이경우 주문 정보가 없으면 주문id를 0으로 나머지는 Null로 구할것. 

SELECT c.customer_id
	, c.contact_name
	, IFNULL(o.order_id, 0) AS order_id 
    , COALESCE(o.order_id, 0) AS order_id_
    , o.order_date
    , CONCAT(e.first_name, ' ', e.last_name) AS employee_name
    , s.company_name AS shipper_name
FROM nw_customers c
	LEFT JOIN nw_orders o ON c.customer_id = o.customer_id
    LEFT JOIN nw_employees e ON e.employee_id = o.employee_id
    LEFT JOIN nw_shippers s ON o.ship_via = s.shipper_id
WHERE c.city = 'Madrid'
;


-- 만일 아래와 같이 중간에 연결되는 집합을 명확히 left outer join 표시하지 않으면 원하는 집합을 가져 올 수 없음. 
select a.customer_id, a.contact_name, coalesce(b.order_id, 0) as order_id, b.order_date
	, c.first_name||' '||c.last_name as employee_name, d.company_name as shipper_name  
from nw_customers a
	left join nw_orders b on a.customer_id = b.customer_id
	join nw_employees c on b.employee_id = c.employee_id
	join nw_shippers d on b.ship_via = d.shipper_id
where a.city = 'Madrid';

-- orders_items에 주문번호(order_id)가 없는 order_id를 가진 orders 데이터 찾기 

SELECT *
FROM nw_orders o
	LEFT JOIN nw_order_items oi ON o.order_id = oi.order_id
WHERE oi.order_id IS NULL
;

-- orders 테이블에 없는 order_id가 있는 order_items 데이터 찾기. 

SELECT *
FROM nw_order_items oi 
	LEFT JOIN nw_orders o ON oi.order_id = o.order_id
WHERE o.order_id IS NULL
;



/************************************
   조인 실습 - Full Outer 조인. 
*************************************/	

-- dept는 소속 직원이 없는 경우 존재. 하지만 직원은 소속 부서가 없는 경우가 없음. 

SELECT d.*
	, e.empno
    , e.ename
FROM hr_dept d
	LEFT JOIN hr_emp e ON d.deptno = e.deptno
;

-- full outer join 테스트를 위해 소속 부서가 없는 테스트용 데이터 생성. 
DROP TABLE IF EXISTS hr_emp_test;
CREATE TABLE hr_emp_test AS SELECT * FROM hr_emp;
SELECT * FROM hr_emp_test;
-- 현재 세션에서만 안전 모드 일시 해제
SET SQL_SAFE_UPDATES = 0;
-- 소속 부서를 Null로 update
UPDATE hr_emp_test SET deptno = NULL WHERE empno = 7934;
SELECT * FROM hr_emp_test ORDER BY 1 DESC;

-- dept를 기준으로 left outer 조인시에는 소속직원이 없는 부서는 추출 되지만. 소속 부서가 없는 직원은 추출할 수 없음.  
SELECT d.*
	, t.empno
    , t.ename
FROM hr_dept d
	LEFT JOIN hr_emp_test t ON d.deptno = t.deptno
;

-- full outer join 하여 양쪽 모두의 집합이 누락되지 않도록 함. 
-- OUTER JOIN은 ORACLE에서만 가능 
-- SELECT d.*
-- 	, t.empno
-- 	, t.ename
-- FROM hr_dept d
-- 	  FULL OUTER JOIN hr_emp_test t ON d.deptno = t.deptno

-- MySQL 에서는 LEFT & RIGHT UNION 해야함
-- LEFT JOIN 결과 (부서 기준, 소속 직원이 없는 부서도 포함)
SELECT d.deptno, d.dname, t.empno, t.ename
FROM hr_dept d
LEFT JOIN hr_emp_test t ON d.deptno = t.deptno

UNION

-- RIGHT JOIN 결과 (직원 기준, 부서가 없는 직원도 포함)
SELECT d.deptno, d.dname, t.empno, t.ename
FROM hr_dept d
RIGHT JOIN hr_emp_test t ON d.deptno = t.deptno;
;

-- FULL OUTER JOIN에는 있지만 LEFT JOIN 에는 없는 친구 구하기 

WITH full_table AS (
	SELECT d.deptno, d.dname, t.empno, t.ename
    FROM hr_dept d
		LEFT JOIN hr_emp_test t ON d.deptno = t.deptno
	UNION
    SELECT d.deptno, d.dname, t.empno, t.ename
    FROM hr_dept d
		RIGHT JOIN hr_emp_test t ON d.deptno = t.deptno
)
, left_table AS (
	SELECT d.deptno, d.dname, t.empno, t.ename
	FROM hr_dept d
		LEFT JOIN hr_emp_test t ON d.deptno = t.deptno
)
SELECT f.* 
FROM full_table f
	LEFT JOIN left_table t ON f.deptno = t.deptno 
WHERE t.deptno IS NULL
;


/************************************
   조인 실습 - Non Equi 조인과 Cross 조인. 
*************************************/

-- 직원정보와 급여등급 정보를 추출. 

SELECT e.*
	, sg.grade as salgrade
FROM hr_emp e
	JOIN hr_salgrade sg ON e.sal BETWEEN sg.losal AND sg.hisal
;

-- 직원 급여의 이력정보를 나타내며, 해당 급여를 가졌던 시점에서의 부서번호도 함께 가져올것.

SELECT *
FROM hr_emp_salary_hist sal 
	JOIN hr_emp_dept_hist dep ON sal.empno = dep.empno 
		AND sal.fromdate BETWEEN dep.fromdate AND dep.todate
ORDER BY 1, 2 
;

-- cross 조인

WITH temp AS(
	SELECT 1 AS rnum 
    UNION ALL 
    SELECT 2 AS rnum 
)
SELECT d.*
	, t.*
FROM hr_dept d 
	CROSS JOIN temp t;


SELECT * FROM hr_emp_dept_hist;
SELECT * FROM hr_emp_salary_hist;
SELECT * FROM nw_customers;
SELECT * FROM nw_orders;
SELECT * FROM nw_employees;
SELECT * FROM nw_order_items;
SELECT * FROM nw_categories;
SELECT * FROM nw_products;
SELECT * FROM nw_shippers;
SELECT * FROM nw_suppliers;
