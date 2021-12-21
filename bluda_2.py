cook_book = {}
def get_indigrients(file_name): 
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            name = line.strip()
            count = int(file.readline().strip())
            list_dish = []
            for indigrients in range(count):
                ingredient_name, quantity, measure = file.readline().split('|')
                sostav =  {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                list_dish.append(sostav)
            cook_book[name] = list_dish
            file.readline()
    return cook_book        

result = get_indigrients('recipes.txt')  
print(result)


def get_shop_list_by_dishes(dishes, person_count):
    shopping = {}
    s_quantity = 0
    for dish, sostav in cook_book.items():
        if dish in dishes:
            for indigrients  in sostav:
                print(indigrients)
                if indigrients == indigrients in sostav:
                    ingredient_name = list(indigrients.values())[0]
                    quantity = (int(list(indigrients.values())[1]) * person_count)
                    s_quantity = (quantity + quantity)
                    measure = list(indigrients.values())[2]
                    shopping[ingredient_name] = {'measure':s_quantity, 'quantity' :measure}
                else:
                    ingredient_name = list(indigrients.values())[0]
                    quantity = (str(list(indigrients.values())[1]) * person_count)
                    measure = list(indigrients.values())[2]
                    shopping[ingredient_name] = {'measure':quantity, 'quantity' :measure} 
                    
    print(shopping)
get_shop_list_by_dishes(['Омлет', 'Омлет'] , 3)
