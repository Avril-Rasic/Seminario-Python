import random 
#Preguntas para el juego 
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena de Python?",
    "¿Cuál de las siguientes opciones es un número entero de Python?", 
    "¿Como se solicita entrada del usuario de Python?", 
    "¿Cuál de las siguientes opciones en un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?"
]
#Respuestas posibles para cada pregunta, en el mismo orden que las preguntas 
answers = [
    ("size()","len()","lenght()","count()"),
    ("3.14","42","10","True"),
    ("input()","scan()","read()","ask()"),
    (
    "// Esto es un comentario", 
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario "
    ),
    ("=","==","!=","==="),
]
#Indice de las respuestas cprrecta para cada pregunta, en el mismo orden que las preguntas

correct_answers_index = [1, 2, 0, 3, 1]

#El usuario debera contestar 3 preguntas

for _ in range(3):
    #Se selcciona una pregunta aleatoria 
    question_index = random.randint(0, len(questions) - 1)

    #Se muestra la pregunta y las respuestas posibles 
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    #El usuario tiene 2 intentos para responder correctamente
    
    for intento in range(2):
        user_answer = int(input("respuesta: ")) - 1
        #Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index[question_index]:
            print("Correcto!!")
            break
        else:
            #Si el usuario no responde correctamente despues de 2 intentos 
            #Se muestra la respuesta correcta
            print("Incorrecto. La respuesta correcta es: ")
            print(answers[question_index][correct_answers_index[question_index]])
    
    #Se imprime in blanco al final de la pregunta
    print()