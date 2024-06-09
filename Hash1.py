# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 

pokemons = [
    {
        "nombre": "Bulbasaur",
        "tipo": "Planta/Veneno",
        "numero_de_pokemon": 1,
        "nivel": 5
    },
    {
        "nombre": "Charmander",
        "tipo": "Fuego",
        "numero_de_pokemon": 4,
        "nivel": 5
    },
    {
        "nombre": "Squirtle",
        "tipo": "Agua",
        "numero_de_pokemon": 7,
        "nivel": 5
    },
    {
        "nombre": "Pikachu",
        "tipo": "Eléctrico",
        "numero_de_pokemon": 25,
        "nivel": 7
    },
    {
        "nombre": "Jigglypuff",
        "tipo": "Normal/Hada",
        "numero_de_pokemon": 39,
        "nivel": 3
    },
    {
        "nombre": "Meowth",
        "tipo": "Normal",
        "numero_de_pokemon": 52,
        "nivel": 4
    },
    {
        "nombre": "Psyduck",
        "tipo": "Agua",
        "numero_de_pokemon": 54,
        "nivel": 6
    },
    {
        "nombre": "Machop",
        "tipo": "Lucha",
        "numero_de_pokemon": 66,
        "nivel": 5
    },
    {
        "nombre": "Geodude",
        "tipo": "Roca/Tierra",
        "numero_de_pokemon": 74,
        "nivel": 4
    },
    {
        "nombre": "Gastly",
        "tipo": "Fantasma/Veneno",
        "numero_de_pokemon": 92,
        "nivel": 6
    },
    {
        "nombre": "Eevee",
        "tipo": "Normal",
        "numero_de_pokemon": 133,
        "nivel": 5
    },
    {
        "nombre": "Snorlax",
        "tipo": "Normal",
        "numero_de_pokemon": 143,
        "nivel": 8
    }
]

# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, 
# en la segunda tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave 
# y la tercera sera en base a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
tabla_tipo = {}
tabla_numero = {}
tabla_nivel={}

# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;

# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
def tipo_s(pokemon):
    tipo=pokemon['tipo']
    if "/" in tipo:
        tipos=tipo.split("/")
        return tipos
    else:
        return tipo

def numero(pokemon):
    numero=pokemon['numero_de_pokemon']
    num=str(numero)
    return num[-1:]

for i in range(1, 11):
    tabla_nivel[i] = []

# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
for pokemon in pokemons:
    tipos=tipo_s(pokemon)
    num=numero(pokemon)
    nivel=pokemon['nivel']

    if type(tipos) == list:
        for tipo in tipos:
            if tipo not in tabla_tipo:
                tabla_tipo[tipo] = []
            tabla_tipo[tipo].append(pokemon)
    else:
        if tipos not in tabla_tipo:
            tabla_tipo[tipos] = []
        tabla_tipo[tipos].append(pokemon)

    if num not in tabla_numero:
        tabla_numero[num] = []
    tabla_numero[num].append(pokemon)

    tabla_nivel[nivel].append(pokemon)

# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
def num379 (tabla_numero):
    print("Los pokemons cuyos numeros terminan en 3 son: ")
    print(tabla_numero['3'])
    print("Los pokemons cuyos numeros terminan en 7 son: ")
    print(tabla_numero['7'])
    print("Los pokemons cuyos numeros terminan en 9 son: ")
    print(tabla_numero['9'])

# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
def multiplos (tabla_nivel):
    print("Los pokemon cuyos niveles son multiplos de 2, 5 o 10 son: ")
    for i in range(1, 11):
        if i%2==0 or i%5==0 or i%10==0:
            print(tabla_nivel[i])

# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo
def acero_fuego_electrico_hielo (tabla_tipo):
    if 'Acero' in tabla_tipo:
        print("Los pokemon de tipo Acero son: ")
        print(tabla_tipo['Acero'])
    if 'Fuego' in tabla_tipo:
        print("Los pokemon de tipo Fuego son: ")
        print(tabla_tipo['Fuego'])
    if 'Eléctrico' in tabla_tipo:
        print("Los pokemon de tipo Electrico son: ")
        print(tabla_tipo['Eléctrico'])
    if 'Hielo' in tabla_tipo:
        print("Los pokemon de tipo Hielo son: ")
        print(tabla_tipo['Hielo'])

num379(tabla_numero)
print()
multiplos(tabla_nivel)
print()
acero_fuego_electrico_hielo(tabla_tipo)
