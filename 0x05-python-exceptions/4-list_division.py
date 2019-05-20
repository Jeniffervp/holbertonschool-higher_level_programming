#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_resul = []
    for a in range(list_length):
        resul = 0
        try:
            resul = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("division by 0")
        finally:
            list_resul.append(resul)
    return list_resul
