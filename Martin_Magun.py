import csv
import random

sueldos_bajos = []
sueldos_medios = []
sueldos_altos = []

trabajadores = [{

    "Nombre" : "Juan Perez",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
},

{

    "Nombre" : "Maria Garcia",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
},

{
    "Nombre" : "Carlos Lopez",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
},

{
    "Nombre" : "Ana Martinez",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
},

{
    "Nombre" : "Pedro Rodriguez",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
},

{
    "Nombre" : "Laura Hernandez",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
},

{
    "Nombre" : "Miguel Sanchez",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
},

{
    "Nombre" : "Isabel Gomez",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
},

{
    "Nombre" : "Francisco Diaz",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
},

{
    "Nombre" : "Elena Fernandez",
    "Sueldo" : 0,
    "Descuento AFP" : 0,
    "Descuento Salud" : 0,
    "Sueldo Liquido" : 0,
}]


def menu ():
    menu_principal = int(input("""

1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa
:"""))
    
    return menu_principal


def asignar_sueldos_aleatorios():

    for i in trabajadores:
        asignar_sueldo_aleatorio = random.randint(300000, 2500000)
        i['Sueldo'] = asignar_sueldo_aleatorio
        
        print (f"\nNombre: {i['Nombre']}  Sueldo: {i['Sueldo']}")
    
    print ("Se asignaron correctamente los sueldos.")


def clasificar_sueldos():

        for clasificar in trabajadores:

            if clasificar['Sueldo'] < 800000:
                sueldos_bajos.append(clasificar)

            elif 800000 < clasificar['Sueldo'] and clasificar['Sueldo'] < 2000000:
                sueldos_medios.append(clasificar)

            elif clasificar['Sueldo'] > 2000000:
                sueldos_altos.append(clasificar)

        print (f"""Sueldos menores a $800.000           Total:{len(sueldos_bajos)}
                
                Nombre                                    Sueldo""")
        for clasificar in sueldos_bajos:
            print (f"""
            {clasificar['Nombre']}                      {clasificar['Sueldo']}""")


        print (f"""Sueldos entre $800.000 y $2.000.000           Total:{len(sueldos_medios)}
                
                Nombre                                      Sueldo""")
        for clasificar in sueldos_medios:
            print (f"""
            {clasificar['Nombre']}                      {clasificar['Sueldo']}""")


        print (f"""Sueldos superiores a $2.000.000          Total:{len(sueldos_altos)}
                
                Nombre                                      Sueldo""")
        for clasificar in sueldos_altos:
            print (f"""
            {clasificar['Nombre']}                      {clasificar['Sueldo']}""")


def estadisticas ():
    
    print ("\n-------- SUELDOS MAS ALTOS --------")
    for i in sueldos_altos:
        print (f"Nombre: {i['Nombre']}      Sueldo: {i['Sueldo']}")
    
    print ("\n-------- SUELDOS MAS BAJOS --------")
    
    for ii in sueldos_bajos:
        print (f"Nombre: {ii['Nombre']}      Sueldo: {ii['Sueldo']}")



def reporte_de_sueldos():
    print ("Nombre empleado:         Sueldo Base:        Descuento Salud:        Descuento AFP Sueldo:          Líquido:")
    for reporte in trabajadores:
        reporte['Descuento AFP'] = reporte['Sueldo'] * 0.12
        reporte['Descuento Salud'] = reporte['Sueldo'] * 0.7

        descuentos_totales = reporte['Descuento AFP'] + reporte['Descuento Salud']

        reporte["Sueldo Liquido"] = reporte["Sueldo"] - descuentos_totales

        print (f"\n{reporte['Nombre']}     \t{reporte['Sueldo']}      \t{reporte['Descuento Salud']}     \t{reporte['Descuento AFP']}       \t{reporte['Sueldo Liquido']}")


    with open ('Trabajadores.cvs', 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(['Nombre', 'Sueldo', 'Descuento AFP', 'Descuento Salud', "Sueldo liquido"])

        for reporte in trabajadores:
            escritor_csv.writerow([reporte['Nombre'],       reporte["Sueldo"],        reporte["Descuento AFP"],       reporte["Descuento Salud"],     reporte["Sueldo Liquido"]])
    
    print ("Descarga exitosa")



try:
    
    while True:
        op = menu()
        print (op)
        
        if op == 1:
            print ("---- ASIGNAR SUELDOS ALEATORIOS ----")
            asignar_sueldos_aleatorios()
            
        elif op == 2:
            print ("---- CLASIFICAR SUELDOS ----")
            clasificar_sueldos()
            
        elif op == 3:
            print ("---- VER ESTADISTICAS ----")
            estadisticas()
            
        elif op == 4:
            print ("---- REPORTE DE SUELDOS ----")
            reporte_de_sueldos()
        elif op == 5:
            print ("""
Finalizando programa…
Desarrollado por Martin Magun
RUT 21.627.439-3""")
            break
                        
        else:
            print ("Seleccione una opcion correcta")
    
except:
    print ("Error")