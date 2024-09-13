from flask import Flask, request, jsonify

app = Flask(__name__)

empleados = [
    {'id':1, 'nombre': 'Devis', 'edad': 28, 'salario': 500000},
    {'id':2, 'nombre': 'Luis', 'edad': 24, 'salario': 1800000},
]

@app.route('/empleados', methods=['GET'])
def obtener_empleados():
    return jsonify(empleados)


@app.route('/empleados', methods=['POST'])
def agregar_empleados():
    nuevo_empleado = request.get_json()
    nuevo_empleado['id'] = len(empleados) + 1
    empleados.append(nuevo_empleado)
    return jsonify(nuevo_empleado),401

@app.route('/empleados/<int:id>', methods=['PUT'])
def actualizar_empleado(id):
    empleado = next((e for e in empleados if e['id']== id), None)
    if empleado is None:
        return jsonify({'mensaje': 'Empleado no encontrado'}),404
    datos = request.get_json()
    empleado.update(datos)
    return jsonify(empleado)


    
@app.route('/empleados/<int:id>', methods=['DELETE'])
def eliminar_empleado(id):
    empleado = next((e for e in empleados if e['id']== id), None)
    if empleado is None:
        return jsonify({'mensaje': 'Empleado no encontrado'}),404 
    empleados.remove(empleado)
    return jsonify({'mensaje':'Empleado eliminado'})

if __name__ == '__main__':
    app.run(debug=True)