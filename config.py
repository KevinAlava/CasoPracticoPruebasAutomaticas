import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/citas_medicas"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "clave_secreta"
