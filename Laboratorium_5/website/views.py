from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from .models import Topic, Thread, Post, User
from . import db
from website.forms import ThreadForm, PostForm

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    topics = Topic.query.all()
    return render_template('home.html', user=current_user, topics=topics)


@views.route('/topic/<int:topic_id>')
@login_required
def topic_view(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    threads = Thread.query.filter_by(topic_id=topic_id).all()
    thread_list = []
    for thread in threads:
        user = User.query.get(thread.user_id)
        thread_dict = {
            'id': thread.id,
            'title': thread.title,
            'author_email': user.email,
            'created_at': thread.date
        }
        thread_list.append(thread_dict)
    return render_template('topic.html', user=current_user, threads=thread_list, topic_id=topic_id)


@views.route('/my-posts')
@login_required
def my_posts_view():
    posts = Post.query.filter_by(user_id=current_user.id).all()
    post_list = []
    for post in posts:
        user = User.query.get(post.user_id)
        thread = Thread.query.get(post.thread_id)
        post_dict = {
            'id': post.id,
            'content': post.content,
            'author_email': user.email,
            'created_at': post.date,
            'thread_title': thread.title
        }
        post_list.append(post_dict)
    return render_template('my_posts.html', user=current_user, posts=post_list)


@views.route('/thread/<int:thread_id>', methods=['GET', 'POST'])
@login_required
def thread_view(thread_id):
    thread = Thread.query.get_or_404(thread_id)
    posts = Post.query.filter_by(thread_id=thread_id).all()
    post_list = []
    for post in posts:
        user = User.query.get(post.user_id)
        post_dict = {
            'id': post.id,
            'content': post.content,
            'author_email': user.email,
            'created_at': post.date
        }
        post_list.append(post_dict)

    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(content=form.content.data, user_id=current_user.id, thread_id=thread_id)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created!', category='success')
        return redirect(url_for('views.thread_view', thread_id=thread_id, thread=thread))
    return render_template('thread.html', user=current_user, posts=post_list, form=form, thread=thread)


@views.route('/topic/<int:topic_id>/create-thread', methods=['GET', 'POST'])
@login_required
def create_thread(topic_id):
    form = ThreadForm()
    if form.validate_on_submit():
        new_thread = Thread(title=form.title.data, user_id=current_user.id, topic_id=topic_id)
        db.session.add(new_thread)
        db.session.flush()
        first_post = Post(content=form.first_post_content.data, user_id=current_user.id, thread_id=new_thread.id)
        db.session.add(first_post)
        db.session.commit()
        flash('Thread created!', category='success')
        return redirect(url_for('views.topic_view', topic_id=topic_id))
    return render_template('create_thread.html', user=current_user, form=form)


@views.route('/thread/<int:thread_id>/delete', methods=['POST'])
@login_required
def delete_thread(thread_id):
    thread = Thread.query.get(thread_id)

    if thread is None:
        flash('Thread not found.', category='error')
    elif thread.user_id != current_user.id:
        flash('You do not have permission to delete this thread.', category='error')
    else:
        db.session.delete(thread)
        db.session.commit()
        flash('Thread deleted.', category='success')

    return redirect(url_for('views.topic_view', topic_id=thread.topic_id, thread=thread))
