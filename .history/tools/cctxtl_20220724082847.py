

#simple tool for downloadnig text in lines
#       used in other functions here

def download_in_lines(file_adress):
    lines=[]

    try:
        with open(file_adress) as file: lines = file.readlines()
        file.close()
        return lines

    except:
        print("Wrong file_adress")
        return 1


#tool for taking words in lines from txt files

def lines_of_words(file_adress):

    lists_of_words=[]

    lines = download_in_lines(file_adress)

    for i in range(len(lines)):

        lists_of_words.append(lines[i].split())

    return lists_of_words

#toll for counting how many words are in every line

def how_many_w_col(lists_of_words):
    
    lists_of_counts=[]

    if (len(lists_of_words[1])==1):
    
        lists_of_words = lines_of_words(lists_of_words)

    for i in range(len(lists_of_words)):

        lists_of_counts.append(len(lists_of_words[i]))

    return lists_of_counts

#toll for reformating list of words to collumns

def words_to_collumns(lists_of_words):

    numbers = how_many_w_col(lists_of_words)

    flag_num=0
    
    for i in range(len(numbers)-1):
    
        flag_num = numbers[i]-numbers[i+1]

    if flag_num!=0:
        print("Different length of each line.")
        return 1
    else:

        coll=[]

        for i in range(numbers[0]):
            
            coll.append([])

            for j in range(len(numbers)):

                coll[i].append(lists_of_words[j][i])

        return coll

