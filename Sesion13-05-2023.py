tupla = ("rojo", "azul", "verde","amarillo")
lista = ["rojo", "azul", "verde","amarillo"]


lista.append('Naranja')


for i in tupla:
    print(i)
    
  
alumnos = [("Juan", [8, 7, 9]), ("María", [6, 9, 7]), ("Pedro", [7, 8, 8])]

for alumno in alumnos:
    nombre = alumno[0]
    notas = alumno[1]
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {round(promedio,2)}")
    

estudiantes = []

while True:
    opcion = input("\nIngrese '1' para agregar un estudiante, '2' para imprimir la base de datos, o '3' para salir: ")
    if opcion == '3':
        break
    elif opcion == '1':
        id = int(input("\nIngrese el número de identificación del estudiante: "))
        nombre = input("\nIngrese el nombre completo del estudiante: ")
        edad = int(input("\nIngrese la edad del estudiante: "))
        semestre = int(input("\nIngrese el semestre actual del estudiante: "))
        materias = []
        while True:
            opcion_materia = input("\nIngrese '1' para agregar una materia, o '3' para salir: ")
            if opcion_materia == '3':
                break
            elif opcion_materia == '1':
                nombre_materia = input("\nIngrese el nombre de la materia: ")
                nota = float(input("\nIngrese la nota obtenida en la materia: "))
                materias.append((nombre_materia, nota))
                
        estudiantes.append((id, nombre, edad, semestre, materias))
    elif opcion == '2':
        for i in estudiantes:
            promedio = sum([materia[1] for materia in i[4]]) / len(i[4])
            print(f"ID: {i[0]}, Nombre: {i[1]}, Edad: {i[2]}, Semestre: {i[3]}, Promedio de notas: {promedio}")

