--
--psql \! chcp 1251
--
--
!сотрудник и годовая зп
SELECT ename AS "имя сотрудника" ,(sal + coalesce(comm,0))*12 AS "Годовая ЗП" FROM emp;
--
--
--
!список должностей по отделам
SELECT job, dname FROM emp, dept WHERE emp.deptno=dept.deptno ORDER BY dname;
--
--
-- 
-- 
!Распечатать список сотрудников, которые были зачислены на работу до января 1979 и 
!после февраля 1981 годов. Результаты упорядочить в порядке убывания даты зачисления на работу
--
SELECT ename, hiredate FROM emp WHERE emp.hiredate::date < '1979-01-01' or emp.hiredate::date > '1981-02-01' ORDER BY hiredate DESC;
--
--
!Вывести сотрудников, которыми никто не руководит.
SELECT ename FROM emp where MGR is null;
--
--
!Определить сотрудников 10 отдела, занимающих должность менеджера или имеющих годовой доход более 3000.
SELECT ename FROM emp where deptno=10 and (job='MANAGER' or (sal + coalesce(comm,0))*12 > 3000);
--
--
!Вывести всех служащих в иерархическом порядке, определяемом должностной подчиненностью
WITH RECURSIVE tree AS (
    SELECT
        empno, ename, mgr, ename AS sort_string, 1 AS depth
    FROM emp
    WHERE mgr IS NULL
    UNION ALL
    SELECT
        s1.empno, s1.ename, s1.mgr,
        (tree.sort_string || '|' || s1.ename)::varchar(10) AS sort_string, tree.depth+1 AS depth
    FROM
        tree
        JOIN emp s1 ON s1.mgr = tree.empno
)

SELECT depth, ename, empno, mgr, sort_string FROM tree ORDER BY sort_string ASC;
--
--
--
!Вычислите и выведите максимальную, среднюю и минимальную зарплату для каждой должности в отделе
SELECT dname, job, MAX(sal + coalesce(comm,0)), min(sal + coalesce(comm,0)), AVG(sal + coalesce(comm,0)) FROM emp, dept WHERE emp.deptno=dept.deptno GROUP BY dname, job ORDER BY dname;
--
--
--
!Определите количество служащих в каждом отделе компании.

SELECT job, count(ename) FROM emp GROUP BY job, job ORDER BY job;
--
--
--
--
!Найдите и распечатайте отделы, в которых работает больше 3-х служащих
--
SELECT job, COUNT(ename) FROM emp GROUP BY job HAVING COUNT(ename) > 3;
--