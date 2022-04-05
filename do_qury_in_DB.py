import psycopg2 as psy

def run_db_query(cursor, text_query):
    #print("Run query on PG")
    cursor.execute(text_query)
    query_result = cursor.fetchall()
    print("Print each row of query result")
    for row in query_result:
        print("n_id  = ", row, "\n")

def main(path_to_querys_file):
        connection_to_pg = psy.connect(user="postgres",
                                      password="postgres",
                                      host="172.23.51.56",
                                      port="5432",
                                      database="esb")
        # open connection to DB
        pg_cursor = connection_to_pg.cursor()

        # get queries from file and run on DB
        with open(path_to_querys_file) as file:
            for index, text_query in enumerate(file):
                try:
                    run_db_query(pg_cursor, text_query)
                except (Exception, psy.Error) as error:
                    if error is ' no results to fetch':
                        pg_cursor.execute("ROLLBACK")
                    else:
                        print("Error from PG-server:", error)
                        pg_cursor.execute("ROLLBACK")

        # close connection to DB
        if connection_to_pg:
            pg_cursor.close()
            connection_to_pg.close()
            print("PostgreSQL connection is closed")
        else:
            print("PostgreSQL connection didn't close")

#if __name__ == '__main__':
#    main(path_to_querys_file)