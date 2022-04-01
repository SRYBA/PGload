# read data from file and write result into new file
def read_all_lines(number_of_lines):
    # variables for partition
    tail1 = ''
    tail2 = ''
    query_row = ''
    # r first line
    with open('C:\\temp\\!1-short.log', 'r', encoding="utf-8") as file_row_data :
        for number_of_lines_culc in range(number_of_lines):
            file_row_string = file_row_data.readline()
            # is there any query?
            if (file_row_string.find(' execute S_')) > -1:
                tail1, tail2, cuted_row = file_row_string.partition(' execute S_')
                cuted_row = cuted_row[3:]
                file_row_string = file_row_data.readline()
                print(file_row_string)
                # is there parametrs?
                if (file_row_string.find('DETAIL: ')) > -1:
                    file_row_string = file_row_string[:-1]
                    list_of_parameters = file_row_string.split(' ')
                    # take parametrs into list
                    for i in range(len(list_of_parameters) - 1, -1, -1):
                        list_of_parameters[i] = list_of_parameters[i].replace(',', '')
                        if list_of_parameters[i].find("'"):
                            del list_of_parameters[i]
                    query_row = cuted_row
                    number_of_param = 1
                    # replace inforation data from query
                    for i in range(len(list_of_parameters) - 1, -1, -1):
                        query_row = query_row.replace('$' + str(number_of_param), list_of_parameters[i])
                        number_of_param += 1
                # wr in file with queries text
                file_query = open('!!query-short.txt', "a")
                file_query.write(query_row)
                file_query.close()

if __name__ == '__main__':
    #main()
    fp = open('C:\\temp\\!1-short.log', 'r', encoding="utf-8")
    number_of_lines = len(fp.readlines())
    fp.close()
    read_all_lines(number_of_lines)

