# redes distribucion logistica

Proyecto Final de la asignatura matemáticas discretas UIS

    ![1687632103310](image/README/1687632103310.png)

**INTRODUCCIÓN:**

La logística y la distribución son aspectos críticos en el funcionamiento eficiente de cualquier empresa, especialmente en aquellas que se dedican a la entrega de productos a múltiples ubicaciones. La optimización de las rutas de distribución es esencial para minimizar los costos de transporte, reducir el tiempo de entrega y mejorar la satisfacción del cliente. En este informe, presentamos una solución al desafío de encontrar la ruta óptima para la logística y distribución de la empresa LogyCo.

El problema abordado en este proyecto involucra la planificación de la mejor ruta para entregar los productos de LogyCo a diferentes destinos. El objetivo principal es encontrar un camino que permita visitar todas las ubicaciones requeridas de manera eficiente, minimizando los costos totales y optimizando el tiempo de entrega. Para lograrlo, se utiliza un algoritmo de búsqueda exhaustiva y técnicas de optimización para encontrar el ciclo hamiltoniano de menor costo.

**DESCRIPCIÓN:**

El modelado del problema se basa en la representación de las ciudades y las conexiones entre ellas mediante una matriz de adyacencia. Esta matriz permite capturar las distancias o costos asociados al transporte entre cada par de ciudades.

El primer paso consiste en ingresar la matriz de adyacencia que contiene la información de las distancias entre las ciudades objetivo. Esta matriz es de tamaño n x n, donde n es el número de ciudades. Cada entrada de la matriz representa la distancia o el costo de transporte entre una ciudad i y una ciudad j.

Para abordar los posibles obstáculos y desafíos logísticos, se simulan eventos aleatorios, como derrumbes y condiciones climáticas adversas. En el caso de los derrumbes, se genera aleatoriamente un porcentaje de ciudades inaccesibles y se las elimina del cálculo del camino óptimo. Esto se logra marcando las conexiones correspondientes en la matriz de adyacencia como inválidas o asignándoles un valor infinito.

En cuanto a las condiciones climáticas adversas, se simula la presencia de lluvia en algunas ciudades seleccionadas aleatoriamente. Para reflejar este escenario, se ajustan los pesos de las rutas correspondientes en la matriz de adyacencia. El ajuste de los pesos se realiza generando un valor aleatorio dentro de un rango definido, que representa el aumento en el tiempo o costo de transporte debido a las condiciones climáticas adversas.

Una vez que se han realizado las modificaciones necesarias en la matriz de adyacencia, se aplica un algoritmo de búsqueda exhaustiva utilizando la técnica de backtracking para encontrar el ciclo hamiltoniano de menor costo. Este algoritmo explora todas las posibles combinaciones de rutas y realiza un seguimiento del costo acumulado y las ciudades visitadas en cada paso. Se actualiza el camino óptimo y el costo mínimo cada vez que se encuentra un ciclo hamiltoniano de menor costo.

Para visualizar la solución encontrada, se utilizan bibliotecas como NetworkX y Matplotlib para generar gráficos que representen el grafo de ciudades y el camino óptimo. Estos gráficos proporcionan una representación visual clara de la distribución de las ciudades y permiten analizar y comprender mejor la solución propuesta.


**OBJETIVOS:**

1. Encontrar la ruta óptima: El objetivo principal de este proyecto es encontrar la ruta óptima para la distribución de productos de la empresa LogyCo. Se busca determinar el recorrido que minimice los costos totales de transporte y optimice el tiempo de entrega, asegurando una distribución eficiente y rentable.
2. Considerar obstáculos logísticos: Se plantea abordar los posibles obstáculos y desafíos logísticos que pueden surgir durante la distribución de productos. Esto incluye la simulación de eventos como derrumbes en carreteras o condiciones climáticas adversas, que pueden afectar la accesibilidad a ciertas ciudades y alterar los tiempos de transporte. El objetivo es ajustar la ruta y los costos en función de estos obstáculos, garantizando una solución realista y adaptada a situaciones imprevistas.
3. Optimizar los recursos de transporte: Se busca optimizar los recursos de transporte disponibles, minimizando los costos asociados a los desplazamientos entre ciudades. Esto implica encontrar la combinación de rutas que permita cubrir todas las ubicaciones requeridas de manera eficiente, evitando trayectos innecesarios y optimizando la capacidad de carga de los vehículos de transporte.
4. Proporcionar resultados numéricos y visuales: Además de encontrar la ruta óptima, se pretende ofrecer resultados numéricos y visualizaciones gráficas que faciliten la comprensión y la toma de decisiones. Se proporcionará información sobre el costo total de transporte, el tiempo estimado de entrega y el camino seguido. Asimismo, se generarán gráficos que representen el grafo de ciudades y el camino óptimo, permitiendo una visualización clara y concisa de la solución propuesta.
5. Mejorar la eficiencia en la logística y distribución: El objetivo final es mejorar la eficiencia en la logística y distribución de LogyCo. Al encontrar la ruta óptima y considerar los obstáculos logísticos, se espera reducir los costos de transporte, acortar los tiempos de entrega y mejorar la satisfacción del cliente. Esta optimización de los procesos de distribución contribuirá a una operación más eficiente y rentable de la empresa.


**MODELO E IMPLEMENTACIÓN DE LA SOLUCIÓN PROPUESTA:**

El modelo de solución propuesto se basa en el uso de un grafo dirigido para representar las ciudades objetivo y las conexiones entre ellas. El grafo se construye utilizando la biblioteca NetworkX en Python. Cada ciudad se representa como un nodo en el grafo, y las distancias entre las ciudades se representan como aristas con pesos.

En la implementación del código proporcionado, se utiliza una matriz de adyacencia para representar el grafo de ciudades. Esta matriz es una estructura bidimensional donde cada entrada (i, j) representa la distancia o el costo de transporte entre la ciudad i y la ciudad j.

El algoritmo principal para encontrar la ruta óptima es un algoritmo de búsqueda exhaustiva con backtracking. La función `find_hamiltonian_cycle()` implementa este algoritmo y recibe como entrada la matriz de adyacencia, una lista de ciudades visitadas, la posición actual, el número total de ciudades, un contador de visitas, el costo acumulado, el ciclo hamiltoniano actual, el camino actual y el camino final.

El algoritmo utiliza un enfoque de backtracking para explorar todas las posibles combinaciones de rutas y encontrar el ciclo hamiltoniano de menor costo. Comienza con una ciudad de partida y verifica todas las ciudades vecinas que no han sido visitadas y tienen una conexión válida en la matriz de adyacencia. Luego, realiza una llamada recursiva a la función `find_hamiltonian_cycle()` para continuar el proceso con la siguiente ciudad. Al regresar de la llamada recursiva, desmarca la ciudad actual como no visitada y retira la última ciudad agregada al camino.

El algoritmo continúa explorando todas las posibles combinaciones hasta que todas las ciudades hayan sido visitadas una vez y se haya regresado al punto de partida. Durante el proceso, se actualiza constantemente el ciclo hamiltoniano de menor costo y se guarda el camino final cuando se encuentra un ciclo de menor costo.

Además de la búsqueda exhaustiva, el código también incorpora elementos de simulación para reflejar obstáculos logísticos y condiciones climáticas adversas. Por ejemplo, se simulan ciudades inaccesibles mediante la eliminación de conexiones en la matriz de adyacencia. Del mismo modo, se simula la presencia de lluvia ajustando los pesos de las rutas correspondientes.

Una vez que se ha encontrado el ciclo hamiltoniano de menor costo, se imprimen los resultados, incluyendo el tiempo total en minutos del recorrido óptimo, el camino seguido y una estimación de los días requeridos para completar la distribución de los productos. Además, se generan gráficos utilizando la biblioteca Matplotlib para visualizar el grafo de ciudades y el camino óptimo.

El código también incluye una GUI (Interfaz Gráfica de Usuario) que muestra la imagen del grafo de ciudades y permite al usuario obtener el camino óptimo. La GUI utiliza la biblioteca Tkinter para crear la interfaz y la biblioteca PIL (Python Imaging Library) para cargar y mostrar las imágenes.


**CONCLUSIONES:**

En el desarrollo de este proyecto de clase, se abordó el problema de encontrar la ruta óptima para la distribución de productos de la empresa LogyCo. A través de la implementación de un algoritmo de búsqueda exhaustiva con backtracking y la simulación de obstáculos logísticos y condiciones climáticas adversas, se logró ofrecer una solución que optimiza los costos de transporte y los tiempos de entrega.

Al finalizar este trabajo, se pueden destacar las siguientes conclusiones:

1. La implementación de algoritmos de búsqueda exhaustiva es una estrategia eficiente para encontrar soluciones óptimas en problemas de optimización combinatoria. En este proyecto, se utilizó el backtracking para explorar todas las posibles combinaciones de rutas y encontrar el ciclo hamiltoniano de menor costo.
2. La simulación de obstáculos logísticos y condiciones climáticas adversas permite obtener soluciones más realistas y adaptadas a situaciones imprevistas. La incorporación de derrumbes en carreteras y la presencia de lluvia en ciudades seleccionadas aleatoriamente enriqueció el modelo y permitió tener en cuenta eventos que podrían afectar la planificación de la distribución.
3. La visualización gráfica de los resultados es una herramienta efectiva para comprender y comunicar la solución propuesta. La generación de gráficos utilizando bibliotecas como NetworkX y Matplotlib permitió representar de manera clara el grafo de ciudades, el camino óptimo y los pesos de las rutas.
4. La GUI proporciona una forma interactiva de obtener el camino óptimo y mejorar la experiencia del usuario. La incorporación de una interfaz gráfica de usuario utilizando Tkinter y PIL permitió que los usuarios puedan interactuar con el programa y obtener resultados de manera más intuitiva.
5. Este proyecto sirvió como una oportunidad para aplicar los conceptos teóricos de optimización combinatoria en un problema práctico de logística y distribución. La capacidad de adaptar el modelo a diferentes escenarios y considerar múltiples factores en la toma de decisiones resultó ser valiosa para encontrar soluciones eficientes y efectivas.

**IMPORTANTE**

Antes de ejecutar el programa , se debe tener en cuenta lo siguiente :

    1. Ejecutar en orden de marcas del archivo main
    Programa principal -> Image source -> GUI

    2. Eliminar los archivos de 'grafo_ciudades.png' y 'grafo_camino.png' si se desea ejecutar el programa
    en una segunda ocasión.

    3. Si se presenta algún error con las imagenes y demás , reiniciar kernel.
