def print_name(name):
    print(name, end=' ')

def make_a_list(*no):
    list_no = []
    for n in no:
        list_no.append(n)
    return list_no


def print_list(list_passed):
    for n in list_passed:
        print(n, end=' ')


