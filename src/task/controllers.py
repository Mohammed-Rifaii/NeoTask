from flask import request, jsonify
import uuid
from .. import db
from .models import Tasks

priority_values = ['low', 'medium', 'high']

#List All Tasks
def list_all_tasks_controller():
    tasks = Tasks.query.all()
    if tasks:
        response = []
        for task in tasks: response.append(task.toDict())
        return jsonify(response)
    else:
        return jsonify({'message': 'No Tasks in the table'}), 404


#Create New Task
def create_task_controller():
    request_form = request.form.to_dict()
    
    title         = request_form['title']
    description   = request_form['description']
    completed_str = request_form['completed']
    priority      = request_form['priority']
    duedate       = request_form['duedate']
    category      = request_form['category']
    
    if priority not in priority_values:
        return jsonify({'message': 'Priority should be low, medium or high'}), 404

    # Convert the string to a boolean value
    completed = completed_str.lower() == 'true'

    new_task = Tasks(title=title, description=description, completed=completed, priority=priority, duedate=duedate,category=category)
    db.session.add(new_task)
    db.session.commit()

    response = new_task.toDict()
    return jsonify(response)


#retrieve specific task Detail
def retrieve_task_controller(task_id):
    task = Tasks.query.get(task_id)
    if task:
        response = task.toDict()
        return jsonify(response)
    else:
        return jsonify({'message': 'No Task with this Id'}), 404


#Put/Update task Detail
def update_task_controller(task_id):
    request_form = request.form.to_dict()
    task = Tasks.query.get(task_id)

    if task :
        task.title           = request_form['title']
        task.description     = request_form['description']
        completed_str        = request_form['completed']
        task.priority        = request_form['priority']

        if task.priority not in priority_values:
            return jsonify({'message': 'Priority should be low, medium or high'}), 404

        task.duedate         = request_form['duedate']
        task.category        = request_form['category']
        task.completed       = completed_str.lower() == 'true'
        db.session.commit()
        response = task.toDict()

        return jsonify(response)
    else:
        return jsonify({'message': 'No Task with this Id'}), 404


#Delete Task
def delete_task_controller(task_id):
    task = Tasks.query.get(task_id)

    if task:
        Tasks.query.filter_by(id=task_id).delete()
        db.session.commit()
        return ('Task with Id "{}" deleted successfully!').format(task_id)
    else :
        return jsonify({'message': 'No Task with this Id'}), 404