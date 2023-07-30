def make_cook_book_1():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for dish in file.read().split('\n\n'):
            dish, _, *ingredients = dish.split('\n')
            cook_book.setdefault(dish, [])
            for raw in ingredients:
                ingredient, quantity, measure = raw.split('|')
                cook_book[dish].append({'ingredient_name': ingredient, 'quantity': int(quantity), 'measure': measure})
    return cook_book

# print(dict(make_cook_book_1().items()))

def make_cook_book_2():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            if line == '\n':
                continue
            else:
                line = line.strip()
                if not line.isdigit():
                    dish = line
                    cook_book.setdefault(dish, [])
                else:
                    for _ in range(int(line)):
                        ingredients = file.readline().strip().split('|')
                        cook_book[dish].append({'ingredient_name': ingredients[0].strip(),
                                                'quantity': int(ingredients[1]),
                                                'measure': ingredients[2].lstrip()})
    return cook_book

# print(make_cook_book_2())

def get_shop_list_by_dishes(dishes, person):
    dishes_filter = dict(filter(lambda item: item[0] in dishes, make_cook_book_1().items()))
    result = {}
    for value in dishes_filter.values():
        for element in value:
            key, quantity, measure = element.values()
            result.setdefault(key, {'measure': measure, 'quantity': 0})
            result[key]['quantity'] += quantity * person
    for key in dict(sorted(result.items())):
        print(key, result[key])

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
