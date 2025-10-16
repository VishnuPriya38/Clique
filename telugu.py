import re
from tamil import tags_clean, connect, upload_to_database
import mysql.connector
from mysql.connector import Error

def code():
    f = open("telugu/tags.txt", "r")

    for x in f:
        indx = x[:4]
        tags = x[3:]

        temp = re.findall(r'\d+', indx)
        res = int(list(map(int, temp))[0])

        tags = tags_clean(tags)

        meme_files = "memes/telugu/" + str(res) + ".jpg"

        print(meme_files)

        conn = connect()
        upload_to_database("Telugu", meme_files, tags, conn)



# code()
