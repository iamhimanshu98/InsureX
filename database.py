import sqlite3
conn = sqlite3.connect("userdata.db")

conn.execute("""
                create table userrecord(
                    name varchar(40),
                    age integer,
                    bmi integer,
                    gender integer,
                    children integer,
                    smoker integer,
                    region text,
                    northwest integer,
                    southeast integer,
                    northeast integer
                    )
            """)

print("Table successfully created in database!")

conn.commit()
conn.close