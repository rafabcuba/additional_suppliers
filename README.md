Solución a la tarea técnica:

Consideraciones generales:
1. El ejercicio se deberá realizar en la versión 14 enterprise.
2. El resultado del ejercicio se deberá entregar en 1 nuevo módulo con la estructura
acorde a los módulos de odoo.
3. Todo el código deberá estar en Inglés.
4. El módulo debe contar con un fichero de traducción es.po
5. El módulo deberá tener como dependencias, el resto de los módulos necesarios
para su correcto funcionamiento.
6. El módulo deberá poder instalarse sin ningún error para poder realizar la revisión de
los ejercicios.
Descripción:
Se necesita adicionar al Sistema un nuevo concepto con denominación “Proveedores
adicionales”
Un proveedor adicional debe tener los campos:
● Partner: (relación con el concepto res.partner del sistema, se selecciona 1 partner).
● Fecha de ingreso al banco de proveedores de la empresa.
● Monto de compra: Monto al que ascienden los pedidos de compras en el que ha
sido vinculado el proveedor adicional.
● Cuenta de gasto: (relación con el concepto cuentas contables del sistema), solo se
deben seleccionar cuentas de tipo gastos.
● Estado: El proveedor adicional, puede pasar por los estados (en proceso,
confirmado, cancelado).
● Permitir mediante botones, transitar por los estados desde el formulario. (el estado
por defecto será “en proceso” desde el mismo se podrá navegar al estado
“confirmado”, desde este estado, se podrá navegar al estado “cancelado”).
Ejercicio 1:
1. Realice una entrada de menú para el concepto “Proveedores adicionales” en la
dirección Compras/Pedidos/Proveedores adicionales.
2. Se debe mostrar las vistas, tree, formulario y kanban
3. Un agrupador por estado del proveedor adicional
4. Un filtro que permite visualizar los proveedores adicionales, que su “Monto de
compra” sea superior a 2000.00 USD.
5. La vista del formulario debe incluir Chatter.
Ejercicio 2:
1. En el concepto Pedidos de compra(Compras/Pedidos/Pedidos de compra), añadir
una nueva pestaña, en la cual se podrá seleccionar varios “Proveedoresadicionales”. Un proveedor adicional puede estar vinculado a varios Pedidos de
compras.
2. Para poder adicionar un “Proveedor adicional” a un pedido de compras, el proveedor
adicional debe estar en el estado “confirmado”
3. Actualmente el sistema permite imprimir la solicitud de compras. A dicho impreso se
le debe adicionar una sección, en la cual se pueda observar los “Proveedores
adicionales” vinculados al Pedido de compras. Por cada “proveedor adicional”,
mostrar el nombre del partner relacionado, la fecha de ingreso y el estado del
mismo.
*Ejercicio 3: => Ejercicio adicional
En el Pedido de compra, en la pestaña donde se mostrarán los “Proveedores adicionales”,
se deberá mostrar un botón llamado contabilizar.
El botón solo será visible si el usuario tiene asignado un nuevo rol llamado: Contabilizar
proveedor adicional. (Se debe crear este nuevo rol)
El botón deberá generar un asiento contable con la siguiente estructura, por cada proveedor
adicional existente en ese Pedido de compra.
Diario: El diario del asiento puede ser cualquiera de tipo: “general”
Cuenta D H
Cuenta de gasto, del proveedor
adicional
Monto total de la
Solicitud de cotización
Cuenta por pagar del proveedor
seleccionado en la Solicitud de
cotización
Monto total de la Solicitud
de cotización