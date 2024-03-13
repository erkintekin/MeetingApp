from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user 
from .models import MeetingData
from . import db
import json
from datetime import datetime

    # Blueprint implementation
views = Blueprint('views',__name__)

        # CRUD methods

    # Create method
@views.route('/', methods = ['GET','POST'])
@login_required
def home():
    user_meetings = current_user.meetings

    if request.method == 'POST':
        name = request.form.get('name')
        date_str = request.form.get('date')

            # Getting datas as a string
        start_time_str = request.form.get('start_time')
        end_time_str = request.form.get('end_time')
        user_id = current_user.id

            # And converting them to date/time for if statement
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        start_time = datetime.strptime(start_time_str, '%H:%M').time()
        end_time = datetime.strptime(end_time_str, '%H:%M').time()

            # Create a new meeting info 
        if date > datetime.now().date():
            if start_time < end_time:
                new_meeting = MeetingData(name=name,date=date_str, start_time=start_time_str, end_time=end_time_str,user_id=user_id)
                db.session.add(new_meeting)
                db.session.commit()
                flash('Meeting added successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                    flash('Sorry! Check your end time!', category='error')
        else:
                    flash('Sorry! Check your date!', category='error')

            # Routing the homepage
    return render_template("home.html",user=current_user, user_meetings=user_meetings) # This checks user is logged in or not


    # Delete method
@views.route('/delete-meeting/<int:id>', methods=['POST'])
@login_required
def delete_meeting(id):
    meeting = MeetingData.query.get(id)
    if meeting and meeting.user_id == current_user.id:
        db.session.delete(meeting)
        db.session.commit()
        return jsonify({})

    # Update method   
@views.route('/update-meeting/<int:id>', methods=['POST'])
@login_required
def update_meeting(id):
    meeting = MeetingData.query.get(id)
    if request.method == 'POST':
        if meeting:
            if meeting.user_id == current_user.id:
                    db.session.delete(meeting)
                    db.session.commit()

                    name = request.form.get('name')
                    date = request.form.get('date')
                    start_time = request.form.get('start_time')
                    end_time = request.form.get('end_time')
                    user_id = current_user.id

                    meeting = MeetingData(name=name, date=date, start_time=start_time, end_time=end_time, user_id=user_id)
                    db.session.add(meeting)
                    db.session.commit()

                    flash('Meeting update is successfull!', category='success')
                    return redirect(url_for('views.home'))
        else:   
            flash('Sorry! Meeting not found', category='error')
    
    return redirect(url_for('views.home'))
