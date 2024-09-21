import pprint

games_dict = {
    'resident evil 4':{
        'yearLaunch': 2023,
        'classification': 9.8,
        'genre': ['açào', 'aventura']
    },
    'mario odyssey':{
        'yearLaunch': 2017,
        'classification': 10.0,
        'genre': ['aventura', '3d']
    },
    'donkey kong country':{
        'yearLaunch': 2017,
        'classification': 10.0,
        'genre': ['aventura', 'plataforma']
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(games_dict)

# 1 - Buscar informação dentro de um dicionário aninhado
print(games_dict['mario odyssey']['genre'])

# 2 - Adicionar um novo item
games_dict['mario odyssey']['player'] = 1
print(games_dict['mario odyssey'])

# 3 - Excluir um dicionario
del games_dict['resident evil 4']
pp.pprint(games_dict)