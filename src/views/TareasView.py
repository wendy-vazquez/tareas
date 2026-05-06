import flet as ft

CLASIFICACIONES = ["deporte", "trabajo", "estudio", "personal", "otros"]

def TareasView(page: ft.Page, tarea_controller, state):
    user = state["user"]
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_lista(user['id_usuario']):
            color = ft.Colors.PINK_200 if t['realizada'] else ft.Colors.PINK_400
            estado = "Hecha" if t['realizada'] else "Pendiente"
            nuevo_estado = 0 if t['realizada'] else 1
            id_tarea = t['id_tarea']

            def toggle_estado(e, id_t=id_tarea, n_estado=nuevo_estado):
                tarea_controller.cambiar_estado(id_t, n_estado)
                refresh()

            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        padding=10,
                        content=ft.ListTile(
                            title=ft.Text(t['descripcion'], weight="bold"),
                            subtitle=ft.Text(t['clasificacion']),
                            trailing=ft.GestureDetector(
                                on_tap=toggle_estado,
                                content=ft.Container(
                                    content=ft.Text(estado, size=12, color=ft.Colors.WHITE),
                                    bgcolor=color,
                                    padding=ft.padding.symmetric(horizontal=8, vertical=4),
                                    border_radius=12,
                                    tooltip="Click para cambiar estado",
                                )
                            ),
                        )
                    )
                )
            )
        page.update()

    txt_desc = ft.TextField(label="Nueva tarea", expand=True)
    dd_clas = ft.Dropdown(
        label="Clasificación", width=160,
        options=[ft.dropdown.Option(c) for c in CLASIFICACIONES],
        value="otros",
    )

    def add_task(e):
        if not txt_desc.value:
            txt_desc.error_text = "Campo requerido"
            page.update()
            return
        txt_desc.error_text = None
        tarea_controller.guardar_nueva(user['id_usuario'], txt_desc.value, dd_clas.value)
        txt_desc.value = ""
        refresh()

    def logout(e):
        state["user"] = None
        page.go("/login")

    refresh()

    return ft.View(
        route="/tareas",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Hola, {user['nombre']} 👋"),
                bgcolor="#C2185B",
                actions=[ft.IconButton(ft.Icons.LOGOUT, tooltip="Cerrar sesión", on_click=logout)]
            ),
            ft.Container(
                padding=20, expand=True,
                content=ft.Column(
                    [
                        ft.Text("Mis Tareas", size=22, weight="bold"),
                        ft.Row([txt_desc, dd_clas, ft.IconButton(ft.Icons.ADD_CIRCLE, on_click=add_task)]),
                        ft.Divider(),
                        lista_tareas,
                    ],
                    expand=True,
                )
            )
        ]
    )
