# def create_an_empty_list():
#     return []
# create_an_empty_list()


def create_a_list():
    new_list = [1, 2, 3, 4]
    my_list = create_a_list()
    print("Initial List:", my_list)
    return new_list

def add_element_to_end_of_list(my_list, element):
    my_list.append(element)
    add_element_to_end_of_list(my_list, 5)
    print("After Adding to End:", my_list)

def add_element_to_start_of_list(my_list, element):
    my_list.insert(0, element)
    add_element_to_start_of_list(my_list, 0)
    print("After Adding to Start:", my_list)

def remove_element_from_end_of_list(my_list):
    if len(my_list) > 0:
        my_list.pop()
        add_element_to_start_of_list(my_list, 0)
        print("After Adding to Start:", my_list)

def remove_element_from_start_of_list(my_list):
    if len(my_list) > 0:
        del my_list[0]
        remove_element_from_end_of_list(my_list)
        print("After Removing from End:", my_list)


def retrieve_first_element_from_list(my_list):
    if len(my_list) > 0:
        return my_list[0]
    return None

def retrieve_element_from_index(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    return None

def retrieve_last_element_from_list(my_list):
    if len(my_list) > 0:
        return my_list[-1]
    return None


 





remove_element_from_start_of_list(my_list)
print("After Removing from Start:", my_list)

first_element = retrieve_first_element_from_list(my_list)
print("First Element:", first_element)

element_at_index_2 = retrieve_element_from_index(my_list, 2)
print("Element at Index 2:", element_at_index_2)

last_element = retrieve_last_element_from_list(my_list)
print("Last Element:", last_element)
