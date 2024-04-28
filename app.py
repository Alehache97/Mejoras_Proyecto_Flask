import os
from flask import Flask, render_template,request
app = Flask(__name__)	

import json
with open("jsonok.json") as fichero:
    jsonok=json.load(fichero)

@app.route('/')
def inicio():
    return render_template("principal.html")

@app.route('/formulario', methods=["GET", "POST"])
def formulario():
    # Inicializar los valores de búsqueda
    buscador = ""
    genero = ""
    categoria = ""

    if request.method == "POST":
        # Obtener datos del formulario
        buscador = request.form.get("busqueda")
        genero = request.form.get("genero")
        categoria = request.form.get("categoria")

        resultados = []

        # Búsqueda de productos según los criterios
        for categoria_key, categoria_info in jsonok["tienda"]["categorias"].items():
            for genero_key, genero_info in categoria_info.items():
                if "productos" in genero_info:
                    for producto in genero_info["productos"]:
                        if (not buscador or producto["nombre"].startswith(buscador)) and \
                           (not genero or genero_key == genero) and \
                           (not categoria or categoria_key == categoria):
                            resultados.append({
                                "id": producto["id"],
                                "nombre": producto["nombre"],
                                "marca": producto["marca"],
                                "precio": producto["precio"],
                                "categoria": categoria_key,
                                "genero": genero_key
                            })

        return render_template("formulario.html", resultados=resultados, buscador=buscador, genero=genero, categoria=categoria)
    else:
        # Renderizar la plantilla con los valores de búsqueda
        return render_template("formulario.html", buscador=buscador, genero=genero, categoria=categoria)



@app.route('/details/<identificador>')
def detalles(identificador):

    listaTallas = []
    listaColores = []

    categorias = ["zapatillas", "camisetas", "sudaderas", "pantalones"]
    generos = ["hombres", "mujeres"]

    for categoria in categorias:
        for genero in generos:
            productos = jsonok["tienda"]["categorias"][categoria][genero]["productos"]
            for producto in productos:
                if int(identificador) == producto["id"]:
                    detalles_producto = producto["detalles"]
                    for talla in detalles_producto["tallas"]:
                        listaTallas.append({"tallas": talla})
                    for color in detalles_producto["colores"]:
                        listaColores.append({"colores": color})

    return render_template("details.html", listaTallas=listaTallas, listaColores=listaColores)

port=os.environ["PORT"]
app.run("0.0.0.0", int(port),debug=True)

