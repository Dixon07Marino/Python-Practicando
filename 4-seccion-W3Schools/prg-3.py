#Modificar dicts

Dixon = {
    "Lastname": "Marino",
    "Age": 19,
    "height": 1.70
}

Dixon["height"] = 1.69

print(Dixon)

Dixon.update({"Lastname": "Sanabria"})

print(Dixon)

#Agregar un nuevo item al dict

Dixon.update({"Job": "Back-End Developer"})

print(Dixon)