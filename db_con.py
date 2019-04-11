import sqlalchemy
from sqlalchemy import create_engine


db_type = "postgres"
db_server = "127.0.0.1"
db_port = "5432"
db_name = "test_db"
db_user = "db_username"
db_password = "db_password"


db_string = '%s://%s:%s@%s:%s/%s' % (db_type, db_user, db_password, db_server, db_port, db_name)


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
