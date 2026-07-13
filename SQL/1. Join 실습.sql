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

SELECT * FROM nw_customers;
SELECT * FROM nw_orders;
SELECT * FROM nw_employees;
SELECT * FROM nw_order_items;
SELECT * FROM nw_categories;
SELECT * FROM nw_products;
SELECT * FROM nw_shippers;
SELECT * FROM nw_suppliers;
