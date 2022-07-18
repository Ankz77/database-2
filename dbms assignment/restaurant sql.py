import csv

from cs50 import SQL
from sqlalchemy import values

open("restaurant_db.db","w").close()

db=SQL("sqlite:///restaurant_db.db")

db.execute("CREATE TABLE customer(id INTEGER, name TEXT, table_no INTEGER, order_to_go TEXT, PRIMARY KEY(id));")

db.execute("CREATE TABLE waiter(id INTEGER PRIMARY KEY, waiters TEXT, customer_id INTEGER, FOREIGN KEY(customer_id) REFERENCES customer(id));")

db.execute("CREATE TABLE food(id INTEGER PRIMARY KEY,cook TEXT, meal TEXT, drink TEXT, amount INTEGER, waiters_id INTEGER, FOREIGN KEY(waiters_id) REFERENCES waiter(id));")

db.execute("CREATE TABLE link(customer_id INTEGER, cook_id INTEGER, waiters_id INTEGER, FOREIGN KEY(customer_id) REFERENCES customer(id), FOREIGN KEY(waiters_id) REFERENCES waiter(id), FOREIGN KEY(cook_id) REFERENCES food(id));")

with open("restaurant.csv", "r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        num1=row["id"]
        cust=row["customer"]
        num2=row["table_no"]
        tab=row["waiters_id"]
        fine=row["waiters"]
        go=row["order_to_go"]
        num3=row["cook_id"]
        chef=row["cook"]
        food=row["meal"]
        soft=row["drink"]
        cost=row["amount"]    

        db.execute("INSERT INTO customer(id,name,table_no,order_to_go) VALUES(?,?,?,?)",num1,cust,num2,go)

        db.execute("INSERT INTO waiter(waiters) VALUES(?)",fine)

        db.execute("INSERT INTO food(cook,meal,drink,amount) VALUES(?,?,?,?)",chef,food,soft,cost)


