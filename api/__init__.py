from flask_restfull import Api

from app import flaskAppInstance
from .Task import Task

restServer =Api(flaskAppInstance)

restServer.add_resource(Task, "/api/v1.0/task")