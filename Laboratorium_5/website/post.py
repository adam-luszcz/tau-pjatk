from flask import Blueprint, request, jsonify
from .models import Thread, Post
from . import db

post = Blueprint('post', __name__)


@post.route('/thread/<int:thread_id>/get-posts')
def get_posts(thread_id):
    posts = Post.query.filter_by(thread_id=thread_id).all()
    post_list = [{'id': post.id, 'content': post.content, 'date': post.date, 'user_id': post.user_id, 'thread_id': post.thread_id} for post in posts]
    return jsonify(post_list)


@post.route('/thread/<int:thread_id>/add-post', methods=['POST'])
def add_post(thread_id):
    data = request.get_json()
    new_post = Post(content=data['content'], thread_id=thread_id, user_id=data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'id': new_post.id, 'content': new_post.content}), 201


@post.route('/get-all-posts')
def get_all_posts():
    posts = Post.query.all()
    post_list = [{'id': post.id, 'content': post.content, 'date': post.date, 'user_id': post.user_id, 'thread_id': post.thread_id, } for post in posts]
    return jsonify(post_list)
