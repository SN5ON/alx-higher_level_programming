#!/usr/bin/python3
# Write a function that divides element by element 2 lists.

def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    ret = 0
    for i in range(0, list_length):
        try:
            ret = (my_list_1[i] / my_list_2[i])
        except TypeError:
            ret = 0
            print("wrong type")
        except ZeroDivisionError:
            ret = 0
            print("division by 0")
        except IndexError:
            ret = 0
            print("out of range")
        finally:
            new_list.append(ret)
    return new_list
