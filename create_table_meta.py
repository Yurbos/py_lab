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


dept = Table('dept', metadata,
    Column('deptno', NUMERIC(4), primary_key=True, comment="код департамента"),
    Column('dname', VARCHAR(14), comment="название департамента"),
    Column('loc', VARCHAR(13), comment="местонахождение")
             )

emp = Table('emp', metadata,
    Column('empno', NUMERIC(4), primary_key=True, comment="код сотрудника"),
    Column('ename', VARCHAR(10), comment="имя сотрудника"),
    Column('job', VARCHAR(9), comment="должность"),
    Column('mgr', NUMERIC(4), comment="руководитель"),
    Column('hiredate', DATE, comment="дата устройства на работу"),
    Column('sal', NUMERIC(7,2), comment="зарплата"),
    Column('comm', NUMERIC(7,2), comment="премия"),
    Column('deptno', NUMERIC(2), ForeignKey("dept.deptno"), comment="код департамента"),
             )

salgrade = Table('salgrade', metadata,
    Column('grade', NUMERIC),
    Column('losal', NUMERIC),
    Column('hisal', NUMERIC)
             )


metadata.create_all(engine)

print("DONE")
