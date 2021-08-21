import sqlite3

class Easy_database:
    def __init__(self, name):
        """
        :param name: name of the actual database, not tables - str
        """
        self.name = name
        self.database = sqlite3.connect(self.name)
        self.c = self.database.cursor()

    def start_of_new_table(self, name, list_of_tuples_name_of_column_value_type):
        """
        If you want to launch a new table without a object, otherwise use create_table_of_an_object_plus_add_in_their_info
        :param name: name of a new table - str
        :param list_of_tuples_name_of_column_value_type: [("name_of_column", "null/integer/real/text/blob")]
        :return: commit
        """
        self.c.execute(f"CREATE TABLE {name} ({list_of_tuples_name_of_column_value_type[0][0]} {list_of_tuples_name_of_column_value_type[0][1]})")
        if len(list_of_tuples_name_of_column_value_type) > 1:
            self.add_columns(name, list_of_tuples_name_of_column_value_type[1:])
        return self.database.commit()

    def _add_one_column(self, name_of_the_table, name_of_column, variable_type):
        """
        this is rather an internal method, because of it´s impracticality
        :param name_of_the_table: str
        :param name_of_column: str
        :param variable_type: null/integer/real/text/blob
        :return: commit
        """
        self.c.execute("""ALTER TABLE {} ADD COLUMN
                    {} {} """.format(name_of_the_table, name_of_column, variable_type))

        return self.database.commit()

    def add_columns(self, name_of_the_table, list_of_tuples_name_of_column_value_type):
        """
        A function to add columns to an already existing table
        :param name_of_the_table: str
        :param list_of_tuples_name_of_column_value_type: [("name_of_column", "null/integer/real/text/blob")]
        :return: commit
        """
        for kw in list_of_tuples_name_of_column_value_type:
            self._add_one_column(name_of_the_table, kw[0], kw[1])

    def add_info(self, name_of_the_table, tuple_of_values):
        """
        :param name_of_the_table:
        :param tuple_of_values:
        :return: commit
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

    def show_everything(self, name_of_table):
        """
        This shows all data from the given table
        :param name_of_table: str
        :return: a list of tuples of data - tuples are divided by columns
        """
        b = self.c.execute(f"SELECT * FROM {name_of_table}")
        return b.fetchall()

    def show_columns(self, name_of_table):
        """
        it creates a tuple of tuples (('ratata', None, None, None, None, None, None), ), i have no idea why it
        behaves like that, but it shows the names of columns, so i guess its sufficient
        :param name_of_table: str
        :return: tuple of columns in a table
        """
        b = self.c.execute(f"SELECT * FROM {name_of_table}")
        return b.description

    def rename_column(self, name, old_column_name, new_column_name):
        """
        :param name: name of table - str
        :param old_column_name: str
        :param new_column_name: str
        :return: commit
        """
        self.c.execute(f"""ALTER TABLE {name} RENAME COLUMN {old_column_name} to {new_column_name}""")
        return self.database.commit()

    def show_specific_columns_data(self, name_of_the_table, column_1, column_2=None, column_3=None, column_4=None, column_5=None, column_6=None, column_7=None):
        """
        If you don't want to see all columns, you can use this method, to access specific columns
        :param name_of_the_table: str
        :param column_1: name - str
        :param column_2: name - str
        :param column_3: name - str
        :param column_4: name - str
        :param column_5: name - str
        :param column_6: name - str
        :param column_7: name - str
        :return: a list of tuples with specific data from specific columns
        """
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

    def create_table_of_an_object(self, obj, list_of_types_in_order):
        """
        It takes object data and sets them as columns in a table
        :param obj: obj with functions name(), data()
        :param list_of_types_in_order:
        :return:
        """
        c = [b for b in dir(obj) if not b.startswith('__') and not callable(getattr(obj, b))]
        b = list(zip(c, list_of_types_in_order))
        self.start_of_new_table(obj.name(), b)
        return

    def add_info_to_table_from_object(self, name, obj):
        """
        it takes data from an object and adds them to a table as data
        :param name: str
        :param obj: obj with functions name(), data()
        :return: commit
        """
        self.add_info(name, obj.data())

    def add_more_info_to_table_from_object(self, name, obj, int):
        """
        if you want a same object´s data more times in a database, you can use this method to add data to a table with
        existing columns,
        :param name: str
        :param obj: obj with functions name(), data()
        :param int: how many times you want to copy the info from object to the table
        :return:
        """
        for i in range(int):
            self.add_info(name, obj.data())

    def create_table_of_an_object_plus_add_in_their_info(self, obj, list_of_types_in_order):
        """
        this function allows you to create a table of an object, plus add their data in
        :param obj: obj with functions name(), data()
        :param list_of_types_in_order: they must be in order, as in method data() - list
        :return: commit
        """
        self.create_table_of_an_object(obj, list_of_types_in_order)
        self.add_info_to_table_from_object(obj.name(), obj.data())

    def create_table_obj_plus_add_info_plus_how_many_times_info(self, obj, list_of_types_in_order, int):
        """
        this function allows you to create a table of an object, plus add their data in and allows you to put the info
        how many times you want
        :param obj: obj with functions name(), data()
        :param list_of_types_in_order: they must be in order, as in method data() - list
        :param int: number of times you want the same object in the table
        :return: commit
        """
        self.create_table_of_an_object(obj, list_of_types_in_order)
        for i in range(int):
            self.add_info_to_table_from_object(obj.name(), obj)

    def close_database(self):
        """
        this command should be issued after every commit to database
        :return:
        """
        self.c.close()
        return

    """  def modify_data(self, table, column, new_data, condition1 , condition2):
            no idea why it doesnt work 
            This is a
            :param table: str
            :param column: str
            :param new_data: str
            :param condition: search condition - something = 5 etc. - str ( if you want to issue None, write Null)
            :return: commit

            self.c.execute(fUPDATE  {table} 
                                SET {column} = {new_data} 
                                WHERE {condition1} = "{condition2}";)
            return self.database.commit()"""











