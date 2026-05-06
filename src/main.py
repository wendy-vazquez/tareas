import flet as ft
from controllers.UsuariosController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.UsuariosView import RegistroView
from views.TareasView import TareasView

def start(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#FF69B4",
            secondary="#FFB6C1",
            surface="#FFF0F5",
        )
    )
    page.bgcolor = "#FFF0F5"
    try:
        auth_ctrl = AuthController()
        tarea_ctrl = TareaController()
    except Exception as e:
        auth_ctrl = None
        tarea_ctrl = None
        print(f"Error BD: {e}")

    # Estado compartido entre vistas
    state = {"user": None}

    def route_change(e):
        page.views.clear()
        if page.route == "/registro":
            page.views.append(RegistroView(page, auth_ctrl, state))
        elif page.route == "/tareas":
            page.views.append(TareasView(page, tarea_ctrl, state))
        else:
            page.views.append(LoginView(page, auth_ctrl, state))
        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change(None)

def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()
