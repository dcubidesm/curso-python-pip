#3.Importas a main y llamas tambien a utils
#importacacion de archivo main.py
import main

#Llamo directamente la función para tener un mejor control de ejecución y NO solo por importarlos
main.run()

#llamamos a "data" desde main
print(main.data)

#Cuando llamamos a main.py en la terminal este no se ejecuta ya que lo controla es un archivo aparte que es
#example.py
#Para ejecutar el main.py aparte de example, se debe crear esa dualidad que se puedaa ejecutar main y example por independiente
