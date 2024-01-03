import copy
from aula160_produtos import produtos

def mudaPreco(produtos):
    new_products = [
        {**produto, 'preco': round(produto['preco'] * 1.1 , 2)}
        for produto in copy.deepcopy(produtos)
    ]
    return new_products

def mostraProdutos(new_products):
    print(*new_products, sep= "\n")
    print()
    return new_products

def sortProducts(new_products):
    mostraProdutos(new_products = sortName(new_products))
    mostraProdutos(new_products= sortValue(new_products))

def sortName(new_products):
    sort_for_name = sorted(
        copy.deepcopy(new_products),
        key = lambda new_products: new_products['nome'],
        reverse = True
    )
    return sort_for_name

def sortValue(new_products):

    sort_for_price = sorted(
        copy.deepcopy(new_products),
        key = lambda new_products: new_products['preco']
    )
    return sort_for_price

print('PRODUTOS ORIGINAIS')
mostraProdutos(produtos)

new_products = mostraProdutos(new_products = mudaPreco(produtos))

sortProducts(new_products)

print('PRODUTOS ORIGINAIS')
mostraProdutos(produtos)