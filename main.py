from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000
USUARIOS = {
    "juan": ("admin", "administrador"),
    "pepe": ("user", "usuario"),
}


def calcular_compra(edad, cantidad):
    total = PRECIO_TARRO * cantidad
    porcentaje = 0

    if edad > 30:
        porcentaje = 25
    elif edad >= 18:
        porcentaje = 15

    descuento = total * porcentaje // 100
    return total, descuento, total - descuento


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    nombre = request.form.get("nombre", "").strip()
    edad = request.form.get("edad", "")
    cantidad = request.form.get("cantidad", "")
    resultado = None
    error = None

    if request.method == "POST":
        try:
            edad_numero = int(edad)
            cantidad_numero = int(cantidad)
            if not nombre or edad_numero < 0 or cantidad_numero < 1:
                raise ValueError
            resultado = calcular_compra(edad_numero, cantidad_numero)
        except ValueError:
            error = "Ingresa un nombre, una edad válida y al menos un tarro de pintura."

    return render_template(
        "ejercicio1.html",
        nombre=nombre,
        edad=edad,
        cantidad=cantidad,
        resultado=resultado,
        error=error,
    )


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre = request.form.get("nombre", "")
    mensaje = None

    if request.method == "POST":
        contrasena = request.form.get("contrasena", "")
        contrasena_guardada, rol = USUARIOS.get(nombre, (None, None))

        if contrasena == contrasena_guardada:
            mensaje = f"Bienvenido {rol} {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", nombre=nombre, mensaje=mensaje)


if __name__ == "__main__":
    app.run()
