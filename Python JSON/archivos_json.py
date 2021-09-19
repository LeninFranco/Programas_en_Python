import json

datasource = {
    "Papitas":[
        {
            "nombre": "Sabritas Clasicas",
            "precio": 12
        },
        {
            "nombre": "Chettos Clasicos",
            "precio": 10
        },
        {
            "nombre": "Takis Fuego",
            "precio": 11
        }
    ],
    "Bebidas":[
        {
            "nombre": "Coca Cola",
            "precio": 14
        },
        {
            "nombre": "Pepsi",
            "precio": 12
        },
        {
            "nombre": "Sprite",
            "precio": 12
        }
    ],
    "Galletas":[
        {
            "nombre": "Emperador",
            "precio": 13
        },
        {
            "nombre": "Chokis",
            "precio": 14
        },
        {
            "nombre": "Canelitas",
            "precio": 13
        }
    ]
}

# Escritura del Archivo Json
with open('datasource.json', 'w') as f:
    json.dump(datasource,f,indent=4) #indent es para dar formato al documento

# Lectura del Archivo Json
with open('datasource.json','r') as f:
    new_datasource = json.load(f)

print(type(new_datasource))
print(new_datasource)