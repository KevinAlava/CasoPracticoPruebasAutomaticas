from extensions import db

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    especialidad = db.Column(db.String(50), nullable=False)

class Consultorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), nullable=False)
    piso = db.Column(db.Integer, nullable=False)

class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id', ondelete="CASCADE"), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id', ondelete="CASCADE"), nullable=False)
    consultorio_id = db.Column(db.Integer, db.ForeignKey('consultorio.id', ondelete="CASCADE"), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
