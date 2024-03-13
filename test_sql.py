import unittest
import sql

class TestSQL(unittest.TestCase):

    def setUp(self):
        self.dbname = "test_db"
        self.table_name = "test_table"
        self.column_name = "test_column"
        self.where = ""

        # Create a test table
        self.create_test_table()

    def tearDown(self):
        # Drop the test table
        self.drop_test_table()

    def create_test_table(self):
        db = sql.connect(host="localhost", user="root", password="root", database=self.dbname)
        cursor = db.cursor()
        cursor.execute("CREATE TABLE %s (%s VARCHAR(255));" %(self.table_name, self.column_name))
        db.close()

    def drop_test_table(self):
        db = sql.connect(host="localhost", user="root", password="root", database=self.dbname)
        cursor = db.cursor()
        cursor.execute("DROP TABLE %s;" %self.table_name)
        db.close()

    def test_select_without_where(self):
        expected_result = [('value1',), ('value2',), ('value3',)]
        result = sql.select(self.dbname, self.table_name, self.column_name, self.where)
        self.assertEqual(result, expected_result)

    def test_select_with_where(self):
        expected_result = [('value2',)]
        where = "test_column = 'value2'"
        result = sql.select(self.dbname, self.table_name, self.column_name, where)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()