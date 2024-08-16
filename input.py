#Haremos un programa interactivo solicitando información al usuario

#Utilizaremos otra función incorporada llamada input que permite obtener la entreada del teclado.

#Las funciones pueden retornar valores. Y esos valores los podemos guardar en la memoria del computador utilizando, inicialmente, variables.

#Asignando el valor de retorno de la función input en una variable name
name = input("¿Cómo te llamas?")
#Luego saludaremos al usuario.
#Llamaremos ala función print con 2 argumentos : "Hola" y el segundo argumento es la variable name
print("Hola", name)
#Puedes escribir un solo argumento con las cadenas de texto f.
print(f"Hola {name}")
