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

1. Mejorar la eficiencia en la entrega de productos: LogiCo busca reducir los tiempos de entrega y minimizar los costos asociados a través de la planificación de rutas óptimas. Al utilizar el algoritmo de Dijkstra, la empresa podrá encontrar las rutas más cortas y eficientes, considerando variables temporales y costos relevantes.
2. Reducir los costos operativos: Al considerar aspectos variables como cierres viales, peajes y condiciones climáticas locales, LogiCo podrá minimizar los costos asociados a la distribución y logística. La planificación de rutas optimizadas permitirá evitar rutas costosas o afectadas por condiciones adversas, lo que resultará en una reducción de los gastos operativos.
3. Adaptarse a situaciones cambiantes: La inclusión de variables temporales en la planificación de rutas permitirá a LogiCo responder de manera eficiente a situaciones imprevistas, como cierres viales o condiciones climáticas adversas. La empresa podrá ajustar las rutas en tiempo real y tomar decisiones informadas para minimizar los impactos negativos en la entrega de productos.
4. Brindar un servicio de calidad: La optimización de las rutas de distribución y logística permitirá a LogiCo ofrecer un servicio más rápido y confiable. Al reducir los tiempos de entrega y mejorar la eficiencia en la distribución de productos, la empresa podrá satisfacer las expectativas y fortalecer su reputación en el mercado.
5. Obtener ventajas competitivas: Al implementar un sistema de distribución y logística optimizado, LogiCo podrá obtener ventajas competitivas en el mercado. La eficiencia en la entrega de productos y la capacidad de adaptarse a situaciones cambiantes brindarán a la empresa una posición sólida frente a la competencia, lo que puede resultar en un aumento de la cuota de mercado y el crecimiento empresarial.

**IMPORTANTE***

Antes de ejecutar el programa , se debe tener en cuenta lo siguiente :

    1. Ejecutar en orden de marcas del archivo main
    Programa principal -> Image source -> GUI

    2. Eliminar los archivos de 'grafo_ciudades.png' y 'grafo_camino.png' si se desea ejecutar el programa
    en una segunda ocasión.

    3. Si se presenta algún error con las imagenes y demás , reiniciar kernel.
