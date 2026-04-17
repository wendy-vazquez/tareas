import flet as ft

def LoginView(page: ft.Page, auth_ctrl):
    email_input = ft.TextField(label="Correo electrónico", width=300, border_radius=10)
    pass_input = ft.TextField(label="Contraseña", width=300, border_radius=10, password=True)
    
    def login_click(e):
        email = email_input.value
        password = pass_input.value
        if auth_ctrl.login(email, password):
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Credenciales incorrectas"))
            page.snack_bar.open = True
            page.update()
    
    return ft.View("/", [
        ft.AppBar(title=ft.Text("Sige - Login"), bgcolor=ft.colors.BLUE_GREY_900, color="white"),
        ft.Column([
            ft.Icon(ft.icons.LOCK_PERSON, size=50, color=ft.colors.BLUE),
            ft.Text("Acceso al Sistema", size=24, weight="bold"),
            email_input,
            pass_input,
            ft.ElevatedButton("Iniciar Sesion", on_click=login_click, width=150),
            ft.TextButton("Crear Cuenta", on_click=lambda e: page.go("/register"))
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER
                 )
    ]
                   )
    