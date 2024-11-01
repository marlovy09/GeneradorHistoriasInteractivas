import random; 

characters = []; 
actions = []; 
places = []; 
loopMenu = True; 
histories = 0; 

def generateHistory() :
    character = random.choice(characters); 
    action = random.choice(actions); 
    place = random.choice(places); 
    
    return f"{character} {action} en {place}."

while (loopMenu):
    characters.append(input("inserta un personaje:")); 

    actions.append(input("\ninserta un accion: ")); 

    places.append(input("\ninserta un lugar: ")); 

    addMore = input("\n¿deses agregar mas personajes? (si/no): "); 
    histories+=1; 

    if(addMore == "no"):
        loopMenu = False; 
        for i in range(histories):
            print(f"""\n
                =========[HISTORIAS RANDOMS]=========
                Historia {i+1}: {generateHistory()}
                =====================================
            """); 
