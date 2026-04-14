import flet as ft
from controllers.UsuariosController import AuthController
from controllers.TareaController import TareaController 
from views.LoginView import LoginView
from views.dashboard import DashboardView

def main(page: ft.Page):
    #instanciamos los controladores una sola vez
    auth_ctrl = AuthController()
    tarea_ctrl = TareaController() 
    
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, auth_ctrl, tarea_ctrl))
        page.update()
    
    page.on_route_change = route_change
    page.go("/")
    
def main():
    #Ejecucion de la app
    ft.app(target=start)

if __name__ == "__main__":
    ft.run(main)
    