import re

def process_message(message, response_array, response):
    #Divide el mensaje y la puntuación en un array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())
    

    #Conteo de las palabras en el mensaje
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    #Respuesta y conteo de palabras en la respuesta
    #print(score, response)
    return [score, response]

def get_response(message):
    #Añadir respuestas
    response_list = [
        process_message(message, ['hello', 'hola', 'ola', 'hi'], 'Hola humano!'),
        process_message(message, ['bye', 'adios'], 'Adios humano!'),
        process_message(message, ['estas'], 'Absolutamente bien!'),
        process_message(message, ['como', 'llamas'], 'Soy el gran Hunab!'),
        process_message(message, ['ayuda', 'ayudame'], 'Vere que puedo hacer!')

    ]

    # Revisar los valores y regresar la mejor respuesta
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Revisar los valores maximos del conteo para la mejor respuesta posible y guardar en variable
    best_response = max(response_scores)
    matching_response = response_list[response_scores.index(best_response)]

    #Regresa el mejor resultado al usuario
    if best_response == 0:
        bot_response = "No entiendo a que te refieres"
    else:
        bot_response = matching_response[1]
    
    print('Bot response: ', bot_response)

    return bot_response

#Test
# get_response('como te llamas')