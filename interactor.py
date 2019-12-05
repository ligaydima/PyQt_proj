import os
import sqlite3

from PIL import Image


class Interactor:
    def __init__(self, db_name, table_name, alt_name="без имени", alt_img="отсутствует"):
        """
        constructor
        :param db_name: name of the database
        :param table_name: name of the table in database
        :param alt_name: title of notification if there's no title entered
        :param alt_img: text returned if there's no image

        """
        self.db_name = db_name
        self.table_name = table_name
        self.alt_name = alt_name
        self.alt_img = alt_img

    def create_if_not_exists(self, cursor, con):
        """
        creates table in db if it does not exist
        :param cursor: sqlite3.connection.cursor
        :param con: sqlite3.connection
        """
        cursor.execute("""CREATE TABLE IF NOT EXISTS "{}" ( 
                        "title" TEXT, 
                        "prior" INTEGER, 
                        "date_time" DATETIME, 
                        "img_name" TEXT );""".format(self.table_name))
        con.commit()

    def exists(self, title, prior, time, img_path):
        """
        check if a notification with given parameters exists or not
        :param title: notification title
        :param prior: notification prior(>=0)
        :param time: datetime (format YYYY-MM-DD HH:MM)
        :param img_path: path to image( empty string if there's no image
        :return: True or False
        """
        if title:
            return len(list(self.get(
                f"SELECT * from {self.table_name} WHERE title='{title}' AND prior={prior} AND date_time=DATETIME('{time}') AND img_name='{img_path}'"))) != 0
        return len(list(self.get(
            f"SELECT * from {self.table_name} WHERE title='{self.alt_name}' AND prior={prior} AND DATETIME(date_time)=DATETIME('{time}') AND img_name='{img_path}'"))) != 0

    def insert(self, title, prior, time, img_path):
        """
        insert notification in db if it does not exist
        :param title: notification title
        :param prior: notification prior(>=0)
        :param time: datetime (format YYYY-MM-DD HH:MM)
        :param img_path: path to image( empty string if there's no image
        """
        if not title:
            title = self.alt_name

        if self.exists(title, prior, time, img_path):
            return
        if img_path:
            im = Image.open(img_path).resize((100, 100))
            try:
                os.mkdir("media")
            except:
                pass
            os.chdir("media")
            new_name = str(title) + str(prior) + time + img_path
            new_name = new_name.replace(":", "")
            new_name = new_name.replace("/", "")
            im.save(new_name)
            os.chdir("..")
        val = (title, prior, time, img_path)
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        self.create_if_not_exists(cursor, con)
        cursor.execute(f"""INSERT INTO {self.table_name} VALUES {val}""")
        con.commit()
        con.close()

    def delete_req(self, req):
        """
        execute deleting query
        :param req: request(SQLite3 syntax)
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        cursor.execute(req)
        con.commit()
        con.close()

    def get(self, req):
        """
        parse db by request
        :param req: request in SQLite3 format
        :return: list
        """
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        self.create_if_not_exists(cursor, con)
        res = cursor.execute(req).fetchall()
        con.close()
        res2 = []
        for i in res:
            i2 = list(i)
            if not i[-1]:
                i2[-1] = self.alt_img
            else:
                i2[-1] = (i[0] + str(i[1]) + i[2] + i[3]).replace(":", "").replace("/", "")
            res2.append(i2)
        return res2
