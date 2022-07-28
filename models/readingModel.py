from db.dbConnection import get_data_sql,get_data


def getStudentList(x):
    qry = 'SELECT name FROM student WHERE id = "{}"'.format(x)

    name = get_data_sql(qry).to_json()
    return name


def getStudentByName(username, password):
    qry = 'SELECT * FROM `user` WHERE name = "{}" AND password = "{}"'.format(username, password)

    user = get_data(qry)
    return user
