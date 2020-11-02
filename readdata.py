from collections import defaultdict
    
def readData(textFileName):
    f = open(textFileName)
    restaurant_cnt = -1
    line_cnt = -1
    item_cnt = 0
    menu = []
    coordinates = []
    
    myData = defaultdict(dict)
    
    for lines in f:
        lines = lines.rstrip('\n')
        if lines == "NEW":
            restaurant_cnt += 1
            line_cnt = 0
            item_cnt = 0
        else:
            if line_cnt == 0:
                #Restaurant name
                myData[restaurant_cnt]['restaurant_name'] = lines     
            elif line_cnt == 1:
                #Restaurant location
                coordinates = lines.split(' ')
                myData[restaurant_cnt]['restaurant_location'] = [int(coordinates[0]), int(coordinates[1])]
            elif line_cnt == 2:
                #Restaurant rating
                myData[restaurant_cnt]['restaurant_rating'] = float(lines)
                myData[restaurant_cnt]['restaurant_menu'] = defaultdict(dict)
            elif line_cnt >= 3:
                #Menu
                if (line_cnt % 2 == 1):
                    menu = lines.split()
                    myData[restaurant_cnt]['restaurant_menu'][item_cnt]['item_name'] = menu[0]
                    myData[restaurant_cnt]['restaurant_menu'][item_cnt]['item_price'] = menu[1]
                    myData[restaurant_cnt]['restaurant_menu'][item_cnt]['item_calories'] = menu[2]
                else:
                    menu = lines.rstrip(' ')
                    menu = menu.split()
                    myData[restaurant_cnt]['restaurant_menu'][item_cnt]['item_ingredients'] = menu
                    item_cnt += 1
          
            line_cnt += 1    
     
    return(myData)



   