import sys
from sqlalchemy import create_engine
from sqlalchemy import text

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
    except Exception:
        print("Could not connect to server")
        return 1
    else:
        print("All right, we here!")
        return 0


def sql_in_file(f_file, session):
    # Open the .sql file
    sql_file = open(f_file, 'r')

    # Create an empty command string
    sql_command = ''

    # Iterate over all lines in the sql file
    for line in sql_file:
        # Ignore commented lines
        if not line.startswith('--') and line.strip('\n'):
            line = line.split('--', 1)[0]
            # Append line to the command string
            sql_command += line.strip('\n')

            # If the command string ends with ';', it is a full statement
            if sql_command.endswith(';'):
                # Try to execute statement and commit it
                try:
                    session.execute(text(sql_command))

                # Assert in case of error
                except Exception as e:
                    print(e)

                # Finally, clear command string
                finally:
                    sql_command = ''


if test_con(db_string) == 1:
    raise SystemExit
else:
    print("test_con PASS")


if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    print("Не указан путь до файла")
    raise SystemExit


try:
    file = open(arg)
except IOError as e:
    print("не удалось открыть файл")
    raise SystemExit
else:
    with file:
        print("Файл найден")
        db = create_engine(db_string)
        sql_in_file(arg, db)


print("ALL DONE!")
