Hi,

This is my Flask project contains a mini-Meeting-website about Online Meeting Organizer.

Let's talk about this Organizer's capabilities:

- Login & Sign Up page
  - Flask Login based.
  - Passwords are hashed as SHA-256 with werkzeug's security.
  - When signing up, duplicate e-mail adresses are not allowed.
  - You must re-enter your password when signing in.

- Homepage
    You can:
    - Create a new meeting but you have to check meeting time and date ! 
    - Delete meetings,
    - Update (edit) meetings,
    - List meetings
   
- GET & POST methods
  - Written with pure Javascript.
 
- Database
  - SQLAlchemy in coding, SQLite for datas.
