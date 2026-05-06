import flet as ft

def LoginView(page: ft.Page, auth_controller, state):

    error_text = ft.Text("", color=ft.Colors.RED_400, size=13)

    email = ft.TextField(
        label="Correo electrónico", width=320,
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        keyboard_type=ft.KeyboardType.EMAIL,
    )
    password = ft.TextField(
        label="Contraseña", width=320,
        prefix_icon=ft.Icons.LOCK_OUTLINED,
        password=True, can_reveal_password=True,
    )
    btn_login = ft.ElevatedButton(
        "Iniciar sesión", width=320, height=45,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    def login_click(e):
        error_text.value = ""
        email.error_text = None
        password.error_text = None

        if not email.value:
            email.error_text = "Campo requerido"
        if not password.value:
            password.error_text = "Campo requerido"
        if email.error_text or password.error_text:
            page.update()
            return

        btn_login.disabled = True
        btn_login.text = "Cargando..."
        page.update()

        try:
            user, msg = auth_controller.login(email.value, password.value)
            if user:
                state["user"] = user
                page.go("/tareas")
            else:
                error_text.value = msg
                btn_login.disabled = False
                btn_login.text = "Iniciar sesión"
                page.update()
        except Exception as ex:
            error_text.value = f"Error de conexión: {str(ex)}"
            btn_login.disabled = False
            btn_login.text = "Iniciar sesión"
            page.update()

    btn_login.on_click = login_click

    return ft.View(
        route="/login",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor=ft.Colors.SURFACE,
        controls=[
            ft.Card(
                elevation=4, width=380,
                content=ft.Container(
                    padding=40,
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.TASK_ALT, size=48, color=ft.Colors.PRIMARY),
                            ft.Text("Bienvenido", size=26, weight="bold"),
                            ft.Text("Inicia sesión para continuar", size=13, color=ft.Colors.SECONDARY),
                            ft.Divider(height=10, color="transparent"),
                            email, password, error_text,
                            ft.Divider(height=4, color="transparent"),
                            btn_login,
                            ft.TextButton(
                                "¿No tienes cuenta? Regístrate",
                                on_click=lambda e: page.go("/registro")
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=12,
                    )
                )
            )
        ]
    )
