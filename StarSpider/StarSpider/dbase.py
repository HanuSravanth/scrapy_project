# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:40:57 2020

@author: hanus
"""

import sqlite3

conn = sqlite3.connect('mystars.db')

curr = conn.cursor()

# curr.execute("""CREATE TABLE STARS_TB
#                           (
#                             STAR_ID         text, 
#                             STAR_NAME       text, 
#                             MAGNITUDE       text,
#                             RIGHT_ASCENSION text,
#                             DECLINATION     text,
#                             LINKS           text
#                             )
#                           """)

print([i for i in curr.execute("""SELECT * FROM STARS_TB""") ])

conn.close()
