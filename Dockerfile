FROM python:3.10.12

# set work directory
WORKDIR /src
# install dependencies
RUN pip freeze > requirements.txt
# copy project
COPY . /src
# run app
CMD ["python", "main.py"]
