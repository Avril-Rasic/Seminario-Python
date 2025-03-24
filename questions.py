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

#selecciona preguntas aleatoria 
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)),k=3)

#El usuario debera contestar 3 preguntas
user_score = 0

for questions, answers, correct_answers_index in questions_to_ask:
    #Se selcciona una pregunta aleatoria 
    question_index = random.randint(0, len(questions) - 1)

    #Se muestra la pregunta y las respuestas posibles 
    print(questions)
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")

    #El usuario tiene 2 intentos para responder correctamente
    
    for intento in range(2):
        user_answer = input("respuesta: ")

        #veo si la rspuesta es correcta
        if (user_answer in ["1", "2", "3", "4"]):
            user_answer = int(user_answer) - 1
        else: 
            print("Respuesta invalida")
            exit(1)

        #Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index:
            print("Correcto!!")
            user_score += 1
            break
        else:
            #Si el usuario no responde correctamente despues de 2 intentos 
            #Se muestra la respuesta correcta
            print("Incorrecto. La respuesta correcta es: ")
            print(answers[correct_answers_index])
            user_score -= 0.5

    #imprimo los puntos que gano
print(f"Usted obtuvo un total de {user_score} puntos!")

    #Se imprime in blanco al final de la pregunta
print()