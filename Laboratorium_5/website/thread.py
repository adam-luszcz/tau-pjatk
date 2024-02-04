from flask import Blueprint, request, jsonify
from .models import Topic, Thread
from . import db

thread = Blueprint('thread', __name__)


@thread.route('/topic/<int:topic_id>/get-threads')
def get_threads(topic_id):
    threads = Thread.query.filter_by(topic_id=topic_id).all()
    thread_list = [{'id': thread.id, 'title': thread.title} for thread in threads]
    return jsonify(thread_list)


@thread.route('/topic/<int:topic_id>/add-thread', methods=['POST'])
def add_thread(topic_id):
    data = request.get_json()
    new_thread = Thread(title=data['title'], topic_id=topic_id, user_id=data['user_id'])
    db.session.add(new_thread)
    db.session.commit()
    return jsonify({'id': new_thread.id, 'title': new_thread.title}), 201
