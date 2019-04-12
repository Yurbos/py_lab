--
--psql \! chcp 1251
--
--
!��������� � ������� ��
SELECT ename AS "��� ����������" ,(sal + coalesce(comm,0))*12 AS "������� ��" FROM emp;
--
--
--
!������ ���������� �� �������
SELECT job, dname FROM emp, dept WHERE emp.deptno=dept.deptno ORDER BY dname;
--
--
-- 
-- 
!����������� ������ �����������, ������� ���� ��������� �� ������ �� ������ 1979 � 
!����� ������� 1981 �����. ���������� ����������� � ������� �������� ���� ���������� �� ������
--
SELECT ename, hiredate FROM emp WHERE emp.hiredate::date < '1979-01-01' or emp.hiredate::date > '1981-02-01' ORDER BY hiredate DESC;
--
--
!������� �����������, �������� ����� �� ���������.
SELECT ename FROM emp where MGR is null;
--
--
!���������� ����������� 10 ������, ���������� ��������� ��������� ��� ������� ������� ����� ����� 3000.
SELECT ename FROM emp where deptno=10 and (job='MANAGER' or (sal + coalesce(comm,0))*12 > 3000);
--
--
!������� ���� �������� � ������������� �������, ������������ ����������� ��������������
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
!��������� � �������� ������������, ������� � ����������� �������� ��� ������ ��������� � ������
SELECT dname, job, MAX(sal + coalesce(comm,0)), min(sal + coalesce(comm,0)), AVG(sal + coalesce(comm,0)) FROM emp, dept WHERE emp.deptno=dept.deptno GROUP BY dname, job ORDER BY dname;
--
--
--
!���������� ���������� �������� � ������ ������ ��������.

SELECT job, count(ename) FROM emp GROUP BY job, job ORDER BY job;
--
--
--
--
!������� � ������������ ������, � ������� �������� ������ 3-� ��������
--
SELECT job, COUNT(ename) FROM emp GROUP BY job HAVING COUNT(ename) > 3;
--