

# Proyecto Final: LinkQueue 馃梻

Una queue es una estructura de datos que utiliza las operaciones de push y pull junto con ser una estructura first in first out (FIFO). 
Para el proyecto se realiz贸 una adpataci贸n del concepto para crear LinkQueue una aplicaci贸n donde el usuario puede guardar los links que ha 
utilizado para sus investigaciones y asignarles un nombre personalizado y as铆 saber de que sitio se trata inmediatamente sin tener un link muy largo. 
Para la versi贸n final, buscando que todo fuera lo m谩s amigable para el usuario, se implement贸 una b煤squeda de links y un ordenamiento por importancia, del 1 al 3. As铆 que el usuario pueda encontrar todo de la manera m谩s f谩cil.

Para esto se aplicaron los conceptos aprendidos en clase como el LinearSearch y SelectionSort los cuales se implementaron para ordenar y buscar en la estructura de linkedList que para el proyecto se implemento como una QUEUE.

Estas dos ultimas funcionalidades solo se implementaron en la version WEB puesto que es donde realmnente funcionan los links. Aunque este proyecto se inicio con una en la terminal que se maneja con comandos que queda como referencia,  y la version actual que es la del navegador que se utiliza con un form. 

### Versi贸n de la terminal

<img src="https://i.imgur.com/sWsT5pK.jpg" width="500" height="280"/>  


### Versi贸n del sitio web

<img src="https://i.imgur.com/oRfJm6h.jpg" width="500" height="280"/>  

## Casos de uso 馃敤

<img src="https://imgur.com/2GeuBzS.jpg" width="400" height="280"/> 

Para los casos de uso se determin贸 que el usuario tendr铆a las opciones de agregar a la cola, eliminar de la cola y mostrar la lista. Adem谩s se agregaron las opciones para que pueda buscar entre los links y agregarles importancia a sus links, del 1 al 3. La computadora se encargar谩 de realizar estas operaciones.



### Videos y links de las pruebas y funcionamiento

- https://youtu.be/zTFZ2IZGZlU -> Video del funcionamiento versi贸n terminal y versi贸n web
- https://youtu.be/bradqAuHfEQ -> Video pruebas JMeter

## Pruebas en JMETER

![image](https://user-images.githubusercontent.com/69205813/119160342-649ca880-ba15-11eb-8e54-b291ea3d60a5.png)
25 usuarios 4 veces

![image](https://user-images.githubusercontent.com/69205813/116155928-0abff180-a6a8-11eb-92f5-ff715d7ff502.png)
1 usuario 100 veces

