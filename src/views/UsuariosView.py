import flet as ft

def RegistroView(page: ft.Page, auth_controller, state):

    error_text = ft.Text("", color=ft.Colors.RED_400, size=13)

    nombre     = ft.TextField(label="Nombre",             width=320, prefix_icon=ft.Icons.PERSON_OUTLINED)
    ap_paterno = ft.TextField(label="Apellido paterno",   width=320, prefix_icon=ft.Icons.PERSON_OUTLINED)
    ap_materno = ft.TextField(label="Apellido materno",   width=320, prefix_icon=ft.Icons.PERSON_OUTLINED)
    usuario    = ft.TextField(label="Nombre de usuario",  width=320, prefix_icon=ft.Icons.ALTERNATE_EMAIL)
    correo     = ft.TextField(label="Correo electrónico", width=320, prefix_icon=ft.Icons.EMAIL_OUTLINED, keyboard_type=ft.KeyboardType.EMAIL)
    contrasena = ft.TextField(label="Contraseña",         width=320, prefix_icon=ft.Icons.LOCK_OUTLINED, password=True, can_reveal_password=True)

    btn_registro = ft.ElevatedButton(
        "Crear cuenta", width=320, height=45,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    def registrar_click(e):
        error_text.value = ""
        for c in [nombre, ap_paterno, usuario, correo, contrasena]:
            c.error_text = None

        vacio = False
        for c in [nombre, ap_paterno, usuario, correo, contrasena]:
            if not c.value:
                c.error_text = "Campo requerido"
                vacio = True
        if vacio:
            page.update()
            return

        btn_registro.disabled = True
        btn_registro.text = "Registrando..."
        page.update()

        try:
            success, msg = auth_controller.registrar_usuario(
                nombre.value, ap_paterno.value, ap_materno.value,
                usuario.value, correo.value, contrasena.value
            )
            if success:
                # Hacer login automático tras registro
                user, _ = auth_controller.login(correo.value, contrasena.value)
                state["user"] = user
                page.go("/tareas")
            else:
                error_text.value = msg
                btn_registro.disabled = False
                btn_registro.text = "Crear cuenta"
                page.update()
        except Exception as ex:
            error_text.value = f"Error: {str(ex)}"
            btn_registro.disabled = False
            btn_registro.text = "Crear cuenta"
            page.update()

    btn_registro.on_click = registrar_click

    return ft.View(
        route="/registro",
        scroll=ft.ScrollMode.AUTO,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Card(
                elevation=4, width=380,
                content=ft.Container(
                    padding=40,
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.TASK_ALT, size=48, color=ft.Colors.PRIMARY),
                            ft.Text("Crear cuenta", size=26, weight="bold"),
                            ft.Text("Regístrate para empezar", size=13, color=ft.Colors.SECONDARY),
                            ft.Divider(height=8, color="transparent"),
                            nombre, ap_paterno, ap_materno,
                            usuario, correo, contrasena,
                            error_text,
                            ft.Divider(height=4, color="transparent"),
                            btn_registro,
                            ft.TextButton(
                                "¿Ya tienes cuenta? Inicia sesión",
                                on_click=lambda e: page.go("/login")
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    )
                )
            )
        ]
    )
