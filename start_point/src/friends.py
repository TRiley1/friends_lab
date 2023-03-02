def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    if food in person["favourites"]["snacks"]:
        return True 
    return False

def add_friend(person, friend_to_add):
    person["friends"].append(friend_to_add)

def remove_friend(person, not_friend):
    person["friends"].remove(not_friend)

def total_money(people):
    result = 0
    for person in people:
        result += person["monies"]
    return result

def lend_money(lender, borrower, value):
    lender["monies"] -= value
    borrower["monies"] += value

def all_favourite_foods(people):
    food_list = []
    for person in people:
        food_list.extend(person["favourites"]["snacks"])
    return food_list

def find_no_friends(people):
    loners = []
    for person in people:
        if len(person["friends"]) == 0:
            loners.append(person)
    return loners

def unique_favourite_tv_shows(people):
    tv_shows = []
    for person in people:
        if person["favourites"]["tv_show"] not in tv_shows:
            tv_shows.append(person["favourites"]["tv_show"])
    return tv_shows

def unique_favourite_tv_shows_bonus(people):
    tv_shows = set()
    for person in people:
        if person["favourites"]["tv_show"] not in tv_shows:
            tv_shows.add(person["favourites"]["tv_show"])
    return tv_shows