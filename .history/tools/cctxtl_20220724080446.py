

#simple tool for downloadnig text in lines

#tool for taking collumns from txt files

def collumns(file_adress):

    lines=[]

    try:
        with open(file_adress) as file: lines = file.readlines()
        file.close()
        return lines
        
    except:
        print("Wrong file_adress")
        return 1

