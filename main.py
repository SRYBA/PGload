from itertools import filterfalse
#open file
file_row_data = open('C:\\temp\\!1-short.log', 'r', encoding='utf-8')
#var for partition
tail1 = ''
tail2 = ''
query_row = ''
#r first line
file_row_string = file_row_data.readline()
#is there query?
if (file_row_string.find(' execute S_')) > -1:
    tail1, tail2, cuted_row = file_row_string.partition(' execute S_')
    cuted_row = cuted_row[3:]
    file_row_string = file_row_data.readline()
    #is there parametrs?
    if (file_row_string.find('DETAIL: ')) > -1:
        file_row_string = file_row_string[:-1]
        list_of_parameters = file_row_string.split(' ')
        #take parametrs into list
        for i in range(len(list_of_parameters) - 1, -1, -1):
            list_of_parameters[i] = list_of_parameters[i].replace(',', '')
            if list_of_parameters[i].find("'"):
                del list_of_parameters[i]

        #replase $x in query
            #print(list_of_parameters)
        query_row = cuted_row
        number_of_param = 1
        for i in range(len(list_of_parameters) - 1, -1, -1):
            query_row = query_row.replace('$' + str(number_of_param), list_of_parameters[i])
            number_of_param += 1
             #print(query_row)
        #print(cuted_row)

    #wr in file with querys text
    file_query = open("C:\\temp\\!!query.txt", "a")
    file_query.write(query_row)
    file_query.close()

        #print('$' + str(number_of_param))
#print(file_row_string)