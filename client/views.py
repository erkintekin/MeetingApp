from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user 
from .models import MeetingData
from . import db
import json

views = Blueprint('views',__name__)


@views.route('/', methods = ['GET','POST'])
@login_required
def home():
    user_meetings = current_user.meetings

    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        user_id = current_user.id
            # Create a new meeting info 
        new_meeting = MeetingData(name=name,date=date, start_time=start_time, end_time=end_time,user_id=user_id)
        db.session.add(new_meeting)
        db.session.commit()

        flash('Meeting added successfully!', category='success')
        return redirect(url_for('views.home'))
    
            # Routing the homepage
    return render_template("home.html",user=current_user, user_meetings=user_meetings) # This checks user is logged in or not

@views.route('/delete-meeting/<int:id>', methods=['POST'])
@login_required
def delete_meeting(id):
    meeting = MeetingData.query.get(id)
    if meeting and meeting.user_id == current_user.id:
        db.session.delete(meeting)
        db.session.commit()
        return jsonify({})
   

