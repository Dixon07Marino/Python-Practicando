listas_tareas = []

programa = 0

def no_hay_tareas():
    print("No hay tareas aún!")

def lista_tareas_completa():
    print(f"Lista de tareas completa: {listas_tareas}")


while programa == 0:
    print("1.Agregar una nueva tarea\n2.Eliminar una tarea usando su posición\n3.Reemplazar una tarea por otra\n4.Mostrar todas las tareas\n5.Eliminar todas las tareas\n6.Salir del programa")

    input_user = input("Elige tu opción colocando el número: ")

    if input_user == "1":
        tarea = input("Coloca la tarea que deseas agregar a la lista: ").strip().capitalize()
        listas_tareas.append(tarea)
        lista_tareas_completa()

    elif input_user == "2":
        if bool(listas_tareas) == False:
            no_hay_tareas()
        else: 
            lista_tareas_completa()
            eliminar_tarea = int(input("Coloca el index/posición de la tarea que desea eliminar: "))
            listas_tareas.pop(eliminar_tarea)
            lista_tareas_completa()

    elif input_user == "3":
        if bool(listas_tareas) == False:
            no_hay_tareas()
        else:
            lista_tareas_completa()
            index_tarea = int(input("Coloca el index/posición de la tarea que deseas reemplazar: "))
            listas_tareas[index_tarea] = input("Escribe tu nueva tarea: ")
            lista_tareas_completa()

    elif input_user == "4":
        if bool(listas_tareas) == False:
            no_hay_tareas()
        else:   
            lista_tareas_completa()
    
    elif input_user == "5":
        if bool(listas_tareas) == False:
            no_hay_tareas()
        else:
            validar = input("Estas seguro? coloca Si/No: ").upper()
            if validar == "SI":
                listas_tareas.clear()

    elif input_user == "6":
        break