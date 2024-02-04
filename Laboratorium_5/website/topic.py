from flask import Blueprint, request, jsonify
from .models import Topic
from . import db

topic = Blueprint('topic', __name__)


@topic.route('/get-topics')
def get_topics():
    topics = Topic.query.all()
    topic_list = []
    for topic in topics:
        topic_dict = {
            'id': topic.id,
            'name': topic.name
        }
        topic_list.append(topic_dict)
    return jsonify(topic_list)


@topic.route('/add-topic', methods=['POST'])
def add_topic():
    data = request.get_json()
    new_topic = Topic(name=data['name'])
    db.session.add(new_topic)
    db.session.commit()

    return jsonify({'id': new_topic.id, 'name': new_topic.name}), 201


@topic.route('/delete-topic/<int:id>', methods=['DELETE'])
def delete_topic(id):
    topic = Topic.query.get_or_404(id)
    db.session.delete(topic)
    db.session.commit()

    return '', 204