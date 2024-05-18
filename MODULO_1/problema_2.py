'''
PROBLEMA 2:

Lee atentamente esta introducción, pues contiene reglas que aplican a la totalidad del presente examen. Un viaje en el Transantiago está dado por una sucesión de tramos. Para caracterizar un tramo de viaje, se especifica el medio de transporte Bus (B), o Metro (M), y el sentido que toma el bus o el metro (S1 ó S2). El bus tiene una tarifa de  640,𝑦𝑒𝑙𝑚𝑒𝑡𝑟𝑜 700. Esto implica que si el viaje parte en bus, y en algún tramo el pasajero combina con el metro, se le cobra un recargo de $60. Si el viaje es iniciado en metro, no hay recargos posteriores por cambio de medio, mientras el pasaje se encuentre vigente. Cada tramo tiene una duración simulada al azar de entre 15 y 70 minutos. Si el tiempo acumulado de viaje excede 120 minutos, el pasaje actual caduca y se debe cobrar un nuevo pasaje al inicio del tramo siguiente, con valor correspondiente al medio respectivo. Por otro lado, si el pasajero en el siguiente tramo toma el mismo medio, pero en dirección distinta, se le cobra un pasaje nuevo1

Escribe un programa en Python que pregunte al usuario tres tramos de viaje en Transantiago (mira ejemplos abajo) y luego despliegue:

True si se cobra tarifa de metro en el primer tramo, o False en caso contrario.
True si se cobra recargo por uso del metro si antes hubo sólo tramos en bus, o False en caso contrario.
True si el tiempo total de viaje excede 120 minutos, o False en caso contrario.
True si se cobra más de un pasaje (por cambio de sentido o tiempo excedido), o False en caso contrario.
El tiempo de cada tramo y total del viaje.
Ejemplos de ejecución:

Ingrese el modo del primer tramo (B/M): B

Ingrese el sentido del primer tramo (S1/S2): S1

Ingrese el modo del segundo tramo (B/M): M

Ingrese el sentido del segundo tramo (S1/S2): S1

Ingrese el modo del tercer tramo (B/M): M

Ingrese el sentido del tercer tramo (S1/S2): S2

False

True

True

True

63 70 50 183

Ingrese el modo del primer tramo (B/M): B

Ingrese el sentido del primer tramo (S1/S2): S1

Ingrese el modo del segundo tramo (B/M): B

Ingrese el sentido del segundo tramo (S1/S2): S2

Ingrese el modo del tercer tramo (B/M): B

Ingrese el sentido del tercer tramo (S1/S2): S1

False

False

False

True

61 39 17 117
'''