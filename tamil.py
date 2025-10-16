# comedy, sad, love, action, angry

import os
import re
import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='clique',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    return conn


def upload_to_database(language, filepath, tag, conn):
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    sql = """INSERT INTO categories(language, filepath, tags) VALUES ('""" + str(language) + """','""" + str(filepath) + """','""" + str(tag).replace("'", '"') + """')"""

    try:
        # Executing the SQL command
        cursor.execute(sql)

        # Commit your changes in the database
        conn.commit()

    except Exception as e:
        print(e)
        # Rolling back in case of error
        conn.rollback()


def tags_clean(tags):
    new_tag = tags
    if new_tag[0].isdigit():
        new_tag = new_tag[1:]

    if new_tag[0] == " ":
        new_tag = new_tag[1:]

    new_tag = new_tag.replace("- ", " - ")
    new_tag = new_tag.replace(" -", " - ")
    new_tag = new_tag.replace("\n", "")
    new_tag = new_tag.replace(") ", "")
    new_tag = new_tag.split(" - ")

    # genres = ["comedy", ["sad", "sentiments", "emotional"], ["love", "romance"], "action", "angry"]
    #
    # if genres in new_tag or genres[1] in new_tag or genres[2] in new_tag:
    #     print(new_tag, genres)


    return new_tag

def code():
    # reading tags
    conn = connect()
    f = open("tamil/tags.txt", "r")

    for x in f:
        indx = x[:3]
        tags = x[2:]

        tags = tags_clean(tags)

        temp = re.findall(r'\d+', indx)
        res = int(list(map(int, temp))[0])

        meme_files = "memes/tamil/" + str(res) + ".jpg"

        upload_to_database("Tamil", meme_files, tags, conn)

# code()