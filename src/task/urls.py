from flask import request
from ..app import app
from .controllers import list_all_tasks_controller, create_task_controller, retrieve_task_controller, update_task_controller, delete_task_controller

@app.route("/tasks", methods=['GET', 'POST'])
def list_create_tasks():
    if request.method == 'GET': return list_all_tasks_controller()
    if request.method == 'POST': return create_task_controller()
    else: return 'Method is Not Allowed'

@app.route("/tasks/<task_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_tasks(task_id):
    if request.method == 'GET': return retrieve_task_controller(task_id)
    if request.method == 'PUT': return update_task_controller(task_id)
    if request.method == 'DELETE': return delete_task_controller(task_id)
    else: return 'Method is Not Allowed'