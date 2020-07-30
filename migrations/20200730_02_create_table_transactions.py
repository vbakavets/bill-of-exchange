from yoyo import step

__depends__ = {'20200730_01_create_table_users'}

steps = [
    step("CREATE TABLE transactions (id integer PRIMARY KEY,"
         "created_by integer,"
         "created_at date,"
         "amount integer,"
         "creditor_id integer,"
         "debtor_id integer,"
         "FOREIGN KEY(created_by) REFERENCES users(id),"
         "FOREIGN KEY(creditor_id) REFERENCES users(id),"
         "FOREIGN KEY(debtor_id) REFERENCES users(id))",
         "DROP TABLE transactions")
]