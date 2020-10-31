import random


Ingredients = { 'meet': { 0: 'beef', 1: 'ham', 2: 'turkey', 3: 'chicken', 4: 'pork', 5: 'bacon', 6: 'lamb'},
'vegetables': {0: 'tomato', 1: 'lettuce', 2: 'cucumber', 3: 'broccoli'},
'dairy' : { 0: 'cheese', 1: 'yogurt', 2: 'milk', 3: 'butter'}

}

def generateData():
    f= open('data.txt','w+')
    
    #Restaurant amount
    cnt_restaurant = random.randint(20, 50)
    
    for i in range(1, cnt_restaurant):
        f.write("NEW" + '\n')
        #Restaurant name (string)
        restaurant_name = "Restaurant" + str(i)
        f.write(restaurant_name + '\n')
        
        #Restaurant locations (int)
        restaurant_location_x = random.randint(0, 500)
        restaurant_location_y = random.randint(0, 500)
        f.write(str(restaurant_location_x) + ' '+ str(restaurant_location_y) + '\n')
        
        #Restaurant ratings (float) (shows only two numbers after decimal)
        restaurant_rating = "{:.2f}".format(random.uniform(1,5))
        f.write(restaurant_rating + '\n')
        
        #Menu items
        cnt_items = random.randint(10, 25)
        f.write(str(cnt_items) + '\n')


        for i in range(1, cnt_items):
            item_ingredients = ['other']
            
            item_name = "Item" + str(i)
            item_price = random.randint(2,10)
            item_calories = random.randint(150, 900)
            
            #Item Ingredients
            used = {}
            meet_cnt = random.randint(0, 3)
            for i in range(0, meet_cnt):
                item_number = random.randint(0, 6)
                if not item_number in used:   
                    item_ingredients.append(Ingredients['meet'][item_number])
                    used[item_number] = 1
                    
            used = {}            
            vegetables_cnt = random.randint(0,2)
            for i in range(0, vegetables_cnt):
                item_number = random.randint(0, 3)
                if not item_number in used:   
                    item_ingredients.append(Ingredients['vegetables'][item_number])
                    used[item_number] = 1 
                    
            used = {}    
            dairy_cnt = random.randint(0,2)
            for i in range(0, dairy_cnt):
                item_number = random.randint(0, 3)
                if not item_number in used: 
                    item_ingredients.append(Ingredients['dairy'][item_number])
                    used[item_number] = 1
            
            f.write(str(item_ingredients) + '\n')
    f.close()
    
generateData()