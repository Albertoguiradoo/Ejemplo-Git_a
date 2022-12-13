import flet as ft


def main(page: ft.Page):
    page.title="Bienvenido a su frutería de confianza!"
    botón_Añadir=ft.FilledButton("Añadir", icon="Añadir")
    def botón_Añadir():
        botón_Añadir.append= dropDownMenúCarnes
        botón_Añadir.append= dropDownMenúVerduras
        botón_Añadir.append= dropDownMenúPescados
        botón_Añadir.append= dropDownMenúSales


    


    #Componente Texto
    texto_Título =ft.Text(value="Buenas caballero, ¿qué desea comprar?", color="black", size=20)
    page.add(texto_Título)#add hace dos cosas: 1- Añadir 2- Actualizar
    
    texto_Título_Sección_Verduras=ft.Text(value="sección de Verduras", color="black", size=20)
    page.add(texto_Título_Sección_Verduras)


    dropDownMenúVerduras = ft.Dropdown(width=300, options=[ft.dropdown.Option("lechuga 0,9$/kg"),
                                                    ft.dropdown.Option("naranjas 2$/kg"),
                                                    ft.dropdown.Option("alcachofas 0,9$/kg"),
                                                    ft.dropdown.Option("moras 50$/kg"),
                                                    ft.dropdown.Option("pepinillos 1,2$/kg"),
                                                    ft.dropdown.Option("tomate para el mejor gazpacho 2$/kg")])
    fila1 = ft.Row(spacing=0, controls=[dropDownMenúVerduras,botón_Añadir] )                                             
    page.add(fila1)
    

    texto_Título_Sección_Pescados=ft.Text(value="sección de Pescados", color="black", size=20)
    page.add(texto_Título_Sección_Pescados)
    dropDownMenúPescados = ft.Dropdown(width=400, options=[ft.dropdown.Option("Almejas 20$/kg"),
                                                    ft.dropdown.Option("Sardinas  50$/kg"),
                                                    ft.dropdown.Option("Calamares 50$/kg"),
                                                    ft.dropdown.Option("Gambones  100$/kg"),
                                                    ft.dropdown.Option("Aleta de Tiburón 5000$/kg"),
                                                    ft.dropdown.Option("Atún Rojo 100.000.$/kg")])
    fila2 = ft.Row(spacing=0, controls=[dropDownMenúPescados,botón_Añadir] )                                             
    page.add(fila2)
    


    texto_Título_Sección_Carnes=ft.Text(value="sección de Carnes", color="black", size=20)
    page.add(texto_Título_Sección_Carnes)
    dropDownMenúCarnes = ft.Dropdown(width=400, options=[ft.dropdown.Option("Pechiga 10$/kg"),
                                                    ft.dropdown.Option("rabo de Toro 50$/kg"),
                                                    ft.dropdown.Option("Carne de Hereford 75$/kg"),
                                                    ft.dropdown.Option("Carne de Angus 100$/kg"),
                                                    ft.dropdown.Option("Carne de Ozaki 50.000$/kg"),
                                                    ft.dropdown.Option("Carne de Kobe 1000.000$/kg")])
    fila3 = ft.Row(spacing=0, controls=[dropDownMenúCarnes,botón_Añadir] )                                             
    page.add(fila3)
    


    texto_Título_Sección_Sales=ft.Text(value="sección de Sales", color="black", size=20)
    page.add(texto_Título_Sección_Sales)
    dropDownMenúSales = ft.Dropdown(width=400, options=[ft.dropdown.Option("Sal marina 1$/kg"),
                                                    ft.dropdown.Option("Sal yodada 1$/kg"),
                                                    ft.dropdown.Option("Sal gruesa o para hornear 1$/kg"),
                                                    ft.dropdown.Option("Sal del Himalaya o sal rosa 10$/kg"),
                                                    ft.dropdown.Option("Sal negra de Hawái 20$/kg"),
                                                    ft.dropdown.Option("Sal ahumada 30$/kg")])
    fila4 = ft.Row(spacing=0, controls=[dropDownMenúSales,botón_Añadir] )                                             
    page.add(fila4)

    texto_Título_Sección_Cervezas=ft.Text(value="sección de Cervezas", color="black", size=20)
    page.add(texto_Título_Sección_Cervezas)
    dropDownMenúCervezas = ft.Dropdown(width=400, options=[ft.dropdown.Option("Mahou 1$/unidad"),
                                                    ft.dropdown.Option("Cruzcampo 1$/unidad"),
                                                    ft.dropdown.Option("Estrella Galicia 10$/unidad"),
                                                    ft.dropdown.Option("Alhambra 10$/unidad"),
                                                    ft.dropdown.Option("Salto Stout 20$/unidad"),
                                                    ft.dropdown.Option("Heineken 30$/unidad")])
    fila5 = ft.Row(spacing=0, controls=[dropDownMenúCervezas,botón_Añadir] )                                             
    page.add(fila5)
        
   


ft.app(target=main)