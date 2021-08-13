import sqlite3

class Easy_database:
    def __init__(self, name):
        self.name = name

    def start(self, *args):
        """
        :param args: it must be in  a format of ("column-name", "variable type")
        :return: a new database file + a table in a name of that database
        """
        conn = sqlite3.connect("{}.db".format(self.name))
        c = conn.cursor()
        c.execute(f"CREATE TABLE {self.name} ({args[0]} {args[1]})")
        return conn.commit()

    def _add_one_column(self, name_of_column, variable_type):
        """
        :param name_of_colum: str
        :param variable_type: BLOB, TEXT, REAL, INTEGER, NULL

        """
        database = sqlite3.connect("{}.db".format(self.name))
        c = database.cursor()
        c.execute("""ALTER TABLE {} ADD COLUMN
                    {} {} """.format(self.name, name_of_column, variable_type))

        return database.commit()

    def add_columns(self, dict_with_columns_name_and_types):
        """
        kwargs: dict in a format of {name:variable type (text, null, integer, blob, real(float))}
        it´s made from _add_one_column for easier work
        """

        for kw, ar in dict_with_columns_name_and_types.items():
            self._add_one_column(kw, ar)

    def add_info(self, *args):
        """
        This function is extremely cumbersome, and not scalable, but for now it´s enough
        :param args: values for columns
        :return: add data to columns
        """
        database = sqlite3.connect("{}.db".format(self.name))
        c = database.cursor()
        t = len(args)
        n = None
        if t == 1:
            c.execute(f"INSERT INTO {self.name} VALUES (?,)", args)
        if t == 2:
            c.execute(f"INSERT INTO {self.name} VALUES (?, ?)", args)
        if t == 3:
            c.execute(f"INSERT INTO {self.name} VALUES (?, ?, ?)", args)
        if t == 4:
            c.execute(f"INSERT INTO {self.name} VALUES (?, ?, ?, ?)", args)
        if t == 5:
            c.execute(f"INSERT INTO {self.name} VALUES (?, ?, ?, ?, ?)", args)
        if t == 6:
            c.execute(f"INSERT INTO {self.name} VALUES (?, ?, ?, ?, ?, ?)", args)
        if t == 7:
            c.execute(f"INSERT INTO {self.name} VALUES (?, ?, ?, ?, ?, ?, ?)", args)

        return database.commit()

    def show_everything(self):
        conn = sqlite3.connect("{}.db".format(self.name))
        c = conn.cursor()
        b = c.execute(f"SELECT * FROM {self.name}")
        return (b.fetchall())

    def rename_columns(self):
        pass

    def modify_data(self):
        pass




"""t = {"name":"text", "class":"integer"}
T = Easy_database("__Student_test")
T.start("id", "integer")
T.add_columns(t)
T.add_info("158", "Alex", "2")
T.add_info("159", "Pepa", "8")
print(T.show_everything())
print(type(T.show_everything()))

"""








