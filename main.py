from client import create_app

app = create_app()

if __name__ == '__main__':  # main.py
    app.run(port= 8000,debug=True) # To run a flask app
    
