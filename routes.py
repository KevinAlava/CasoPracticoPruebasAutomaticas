from flask_restful import Api, Resource, reqparse
from extensions import db
from models import Paciente, Medico, Consultorio, Cita

api = Api()

paciente_parser = reqparse.RequestParser()
paciente_parser.add_argument("nombre", type=str, required=True, help="Nombre es obligatorio")
paciente_parser.add_argument("apellido", type=str, required=True, help="Apellido es obligatorio")
paciente_parser.add_argument("fecha_nacimiento", type=str, required=True, help="Fecha de nacimiento es obligatoria")
paciente_parser.add_argument("email", type=str, required=True, help="Email es obligatorio")

class PacienteResource(Resource):
    def get(self, paciente_id=None):
        if paciente_id:
            paciente = Paciente.query.get(paciente_id)
            return paciente.__dict__ if paciente else {"error": "Paciente no encontrado"}, 404
        pacientes = Paciente.query.all()
        return [{"id": p.id, "nombre": p.nombre, "apellido": p.apellido, "email": p.email} for p in pacientes]

    def post(self):
        args = paciente_parser.parse_args()
        nuevo_paciente = Paciente(**args)
        db.session.add(nuevo_paciente)
        db.session.commit()
        return {"message": "Paciente agregado correctamente"}, 201

api.add_resource(PacienteResource, "/pacientes", "/pacientes/<int:paciente_id>")
