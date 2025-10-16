import re
from tamil import tags_clean, connect, upload_to_database
import mysql.connector
from mysql.connector import Error

def code():
    f = open("hindi/tags.txt", "r")

    for x in f:
        indx = x[:4]
        tags = x[3:]

        temp = re.findall(r'\d+', indx)
        res = int(list(map(int, temp))[0])

        tags = tags_clean(tags)

        meme_files = "memes/hindi/" + str(res) + ".jpg"

        # print(tags)

        conn = connect()
        upload_to_database("Hindi", meme_files, tags, conn)



# code()
