# import copy

# def changeAge(people):
#     new_people = [
#         {**pessoa, 'age': pessoa['age'] + 1}
#         for pessoa in copy.deepcopy(people)
#     ]
#     return new_people

# people = [
#     {'name': 'Wendell', 'age': 19},
#     {'name': 'William', 'age': 27},
#     {'name': 'Mariete', 'age': 49},
#     {'name': 'Nivair', 'age': 55}
# ]
# new_people = changeAge(people)
# print(*new_people, sep="\n")



def principal(funcao, x):
    def interna(y):
        return funcao(x,y)
    return interna

@principal
def soma (x,y):
    return x+y

soma_com_cinco = principal(soma,5)

print(soma_com_cinco(20))