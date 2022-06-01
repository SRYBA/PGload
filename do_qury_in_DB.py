import psycopg2 as psy
import datetime as time
from threading import Thread

path_to_querys_file = 'C:\\Users\\RybakSA\\Desktop\\Скрипты постгрес\\!!!!!work\\1с\\logs\\!query.txt'

def run_db_query(cursor, text_query):
    #print("Run query on PG")
    cursor.execute(text_query)
    query_result = cursor.fetchall()
    #testing output
    #print("Print each row of query result")
    #for row in query_result:
    #    print("n_id  = ", row, "\n")

def main(path_to_querys_file):
        #test conection to DB
        connection_to_pg = psy.connect(user="postgres",
                                      password="Gazprom09",
                                      host="192.168.102.131",
                                      port="5432",
                                      database="esb")
        # open connection to DB
        pg_cursor = connection_to_pg.cursor()

        # get queries from file and run on DB
        with open(path_to_querys_file) as file:
            for index, text_query in enumerate(file):
                try:
                    run_db_query(pg_cursor, text_query)
                    #time.sleep(0.001)
                except (Exception, psy.Error) as error:
                    if error is ' no results to fetch':
                        pg_cursor.execute("ROLLBACK")
                    else:
                        # testing output
                        # print("Error from PG-server:", error)
                        pg_cursor.execute("ROLLBACK")

        # close connection to DB
        if connection_to_pg:
            pg_cursor.close()
            connection_to_pg.close()
            print("PostgreSQL connection is closed")
        else:
            print("PostgreSQL connection didn't close")
        return

if __name__ == '__main__':
    start_time = time.datetime.now()

    # starting parallel threads
    processThread = Thread(target=main(path_to_querys_file))
    processThread2 = Thread(target=main(path_to_querys_file))
    processThread3 = Thread(target=main(path_to_querys_file))
    processThread4 = Thread(target=main(path_to_querys_file))
    #print("run 1")
    processThread.start()
    #print("run 2")
    processThread2.start()
    processThread3.start()
    processThread4.start()
    processThread.join()
    processThread2.join()
    processThread3.join()
    processThread4.join()

    # show time of working
    print("Start time:%s:%s:%s" % (start_time.hour, start_time.minute, start_time.second))
    print("End time:%s:%s:%s" % (time.datetime.now().hour, time.datetime.now().minute, time.datetime.now().second))