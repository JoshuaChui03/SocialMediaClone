import sqlite3
from Controllers.login_screen_actions import *
from Controllers.home_screen_actions import *

conn = None
cursor = None


def connect(path):
    global conn, cursor

    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    conn.commit()
    return


def main():
    global conn, cursor
    exit_program = False

    path = input("Enter the relative path of the database you want to run the application on: ")
    # ./prj-db.db
    try:
        connect(path)
    except:
        print("Problems accessing data base \"{}\"".format(path))
        exit()

    while True:
        user, exit_program = login_screen(conn, cursor)

        if not exit_program:
            home_screen(conn, cursor, user)
        else:
            break

    conn.commit()
    conn.close()
    print("\nThanks for using our social media app!!\n")
    return


if __name__ == "__main__":
    main()
