from sqlalchemy import *
metadata = MetaData()


db_type = "postgres"
db_server = "127.0.0.1"
db_port = "5432"
db_name = "test_db"
db_user = "db_username"
db_password = "db_password"

db_string = '%s://%s:%s@%s:%s/%s' % (db_type, db_user, db_password, db_server, db_port, db_name)

engine = create_engine(db_string)


def test_con(test_string):
    try:
        db_test = create_engine(test_string)
        db_test.connect()
    except Exception as e:
        print(e)
        return 1
    else:
        print("All right, we here!")
        return 0


if test_con(db_string) == 1:
    raise SystemExit

print("stay here!")


dept = Table('DEPT', metadata,
    Column('DEPTNO', NUMERIC(4), primary_key=True),
    Column('DNAME', VARCHAR(14)),
    Column('LOC', VARCHAR(13),)
             )

emp = Table('EMP', metadata,
    Column('EMPNO', NUMERIC(4), primary_key=True),
    Column('ENAME', VARCHAR(10)),
    Column('JOB', VARCHAR(9)),
    Column('MGR', NUMERIC(4)),
    Column('HIREDATE', DATE),
    Column('SAL', NUMERIC(7,2)),
    Column('COMM', NUMERIC(7,2)),
    Column('DEPTNO', NUMERIC(2), ForeignKey("DEPT.DEPTNO")),
             )

salgrade = Table('SALGRADE', metadata,
    Column('GRADE', NUMERIC),
    Column('LOSAL', NUMERIC),
    Column('HISAL', NUMERIC)
             )


metadata.create_all(engine)

print("DONE")
