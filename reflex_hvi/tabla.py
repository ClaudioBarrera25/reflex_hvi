import reflex as rx


class Paciente(rx.Base):
    nombre: str
    raza: str


class AppState(rx.State):
    pacientes: list[Paciente] = [
        Paciente(nombre="Firulais", raza="Mestizo"),
        Paciente(nombre="Luna", raza="Labrador"),
        Paciente(nombre="Michi", raza="Siamés"),
    ]


def tabla_pacientes() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Raza"),
            )
        ),
        rx.table.body(
            rx.foreach(
                AppState.pacientes,
                lambda p: rx.table.row(
                    rx.table.cell(p.nombre),
                    rx.table.cell(p.raza),
                ),
            )
        ),
        width="100%",
    )


def index() -> rx.Component:
    return rx.container(
        rx.heading("Pacientes", size="7"),
        tabla_pacientes(),
        margin_top="2em",
    )


app = rx.App()
app.add_page(index)
