import sqlite3

class Easy_database:
    def __init__(self, name):
        self.name = name
        self.database = sqlite3.connect(self.name)
        self.c = self.database.cursor()

    def start_of_new_table(self, name, list_of_tuples_name_of_column_value_type):
        """
        :param args: it must be in  a format of ("column-name", "variable type")
        :return: a new database file + a table in a name of that database
        """
        self.c.execute(f"CREATE TABLE {name} ({list_of_tuples_name_of_column_value_type[0][0]} {list_of_tuples_name_of_column_value_type[0][1]})")

        if len(list_of_tuples_name_of_column_value_type) > 1:
            self.add_columns(name, list_of_tuples_name_of_column_value_type[1:])
        return self.database.commit()

    def _add_one_column(self, name_of_the_table, name_of_column, variable_type):
        """
        :param name_of_colum: str
        :param variable_type: BLOB, TEXT, REAL, INTEGER, NULL

        """
        self.c.execute("""ALTER TABLE {} ADD COLUMN
                    {} {} """.format(name_of_the_table, name_of_column, variable_type))

        return self.database.commit()

    def add_columns(self, name_of_the_table, list_of_tuples_name_of_column_value_type):
        """
        kwargs: dict in a format of {name:variable type (text, null, integer, blob, real(float))}
        it´s made from _add_one_column for easier work
        """

        for kw in list_of_tuples_name_of_column_value_type:
            self._add_one_column(name_of_the_table, kw[0], kw[1])

    def add_info(self, name_of_the_table, tuple_of_values):
        """
        This function is extremely cumbersome, and not scalable, but for now it´s enough
        :type args: object
        :param args: values for columns
        :return: add data to columns
        """
        t = len(tuple_of_values)
        if t == 1:
            self.c.execute(f"INSERT INTO {name_of_the_table} VALUES (?)", tuple_of_values)
        if t == 2:
            self.c.execute(f"INSERT INTO {name_of_the_table} VALUES (?, ?)", tuple_of_values)
        if t == 3:
            self.c.execute(f"INSERT INTO {name_of_the_table} VALUES (?, ?, ?)", tuple_of_values)
        if t == 4:
            self.c.execute(f"INSERT INTO {name_of_the_table} VALUES (?, ?, ?, ?)", tuple_of_values)
        if t == 5:
            self.c.execute(f"INSERT INTO {name_of_the_table} VALUES (?, ?, ?, ?, ?)", tuple_of_values)
        if t == 6:
            self.c.execute(f"INSERT INTO {name_of_the_table} VALUES (?, ?, ?, ?, ?, ?)", tuple_of_values)
        if t == 7:
            self.c.execute(f"INSERT INTO {name_of_the_table} VALUES (?, ?, ?, ?, ?, ?, ?)", tuple_of_values)

        return self.database.commit()

    def show_everything(self):
        b = self.c.execute(f"SELECT * FROM {self.name}")
        return b.fetchall()

    def rename_columns(self, name, old_column_name, new_column_name):
        self.c.execute(f"""ALTER TABLE {name} RENAME COLUMN {old_column_name} to {new_column_name}""")
        return self.database.commit()

    def show_specific_columns(self, name_of_the_table, column_1, column_2=None, column_3=None, column_4=None, column_5=None, column_6=None, column_7=None):
        if column_2 is None:
            a = self.c.execute(f"""SELECT {column_1} FROM {name_of_the_table}""")
            return a.fetchall()
        if column_3 is None:
            a = self.c.execute(f"""SELECT {column_1} , {column_2}  FROM {name_of_the_table}""")
            return a.fetchall()
        if column_4 is None:
            a = self.c.execute(f"""SELECT {column_1} , {column_2}, {column_3} FROM {name_of_the_table}""")
            return a.fetchall()
        if column_5 is None:
            a = self.c.execute(f"""SELECT {column_1}, {column_2}, {column_3}, {column_4} FROM {name_of_the_table}""")
            return a.fetchall()
        if column_6 is None:
            a = self.c.execute(f"""SELECT {column_1}, {column_2}, {column_3}, {column_4}, {column_5} FROM {name_of_the_table}""")
            return a.fetchall()
        if column_7 is None:
            a = self.c.execute(f"""SELECT {column_1}, {column_2}, {column_3}, {column_4}, {column_5}, {column_6} FROM {name_of_the_table}""")
            return a.fetchall()
        else:
            a = self.c.execute(f"""SELECT {column_1}, {column_2}, {column_3}, {column_4}, {column_5}, {column_6}, {column_7} FROM {name_of_the_table}""")
            return a.fetchall()

    def modify_data(self):
        pass

    def create_table_of_an_object(self, obj, list_of_types_in_order):
        c = [b for b in dir(obj) if not b.startswith('__') and not callable(getattr(obj, b))]
        b = list(zip(c, list_of_types_in_order))
        self.start_of_new_table(obj.name(), b)
        return

    def add_info_to_table_from_object(self, name, obj):
        self.add_info(name, obj.data())
        len(obj.data())

    def add_more_info_to_table_from_object(self, name, obj, int):
        for i in range(int):
            a = len(obj.data())
            self.add_info(name, obj.data())

    def create_table_of_an_object_plus_add_in_their_info(self, obj, list_of_types_in_order):
        self.create_table_of_an_object(obj, list_of_types_in_order)
        self.add_info_to_table_from_object(obj.name(), obj.data())

    def create_table_obj_plus_add_info_plus_how_many_times_info(self, obj, list_of_types_in_order, int):
        self.create_table_of_an_object(obj, list_of_types_in_order)
        for i in range(int):
            self.add_more_info_to_table_from_object(obj.name(), obj, int)

    def close_database(self):
        self.c.close()
        return


"""
list_fo_tuples = [("ratata", "text")]
b = ("R")
t = Easy_database("__TStudent_test.db")

t.start_of_new_table("studenti", list_fo_tuples)
t.add_info("studenti", b)
#t.test_add_info("studenti", b)
print(t.show_specific_columns("studenti", "ratata"))


class Student:
    def __init__(self, jméno, věk, škola):
        self.jméno = jméno
        self.věk = věk
        self.škola = škola

    def name(self):
        return "Student"

    def data(self):
        return self.jméno, self.věk, self.škola

a = Student("Pepa", 3, "kocourkov")
r = ("text", "integer", "text")
#t.create_table_obj_plus_add_info_plus_how_many_times_info(a, r, 5)
"""











