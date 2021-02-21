from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


#Steps to run:-

# 1. Goto Terminal
# 2. Set directory to where Flash program is present
# 3. Set flask Environment variable with the command  -> set FLASK_APP=run.py
# 4. Once env variable set type flask run to run the program
# 5. When run it provides IP and port number for e.g.http://127.0.0.1:5000/ where
#
#   127.0.0.1 =IP
#   5000 = Port
# If user runs http://localhost:5000/ then also it has the same result

# If user wishes to run app in DEBUG mode then set environment variable FLASK_DEBUG=1  using command set FLASK_DEBUG=1

# If app is run in Debug mode then changes made in code will be reflected by automatically refreshing webpage
# User does not need to  run the flask run command again

# RUN DIRECTLY WITHOUT SETTING ENVIRONMENT VARIABLES
# Use command:-

# if __name__ == '__main__':
#     app.run(debug=True)
# In Terminal just write python program_name.py and it will run the same way


