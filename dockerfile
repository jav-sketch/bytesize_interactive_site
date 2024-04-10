#
FROM python:3.12.2-bullseye

#set working directory 
WORKDIR /app
 
# Copies requirements.txt to the working directory
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copies the rest of your app's source code from your host to your image filesystem.
COPY . .

# Run the application and expose port 8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]