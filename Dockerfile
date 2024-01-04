FROM python:3.10.12

COPY requirements.txt /requirements.txt

# set work directory
WORKDIR /src
# install dependencies
RUN pip install -r requirements.txt
# copy project
COPY . /src
# run app
CMD ["python", "src/main.py"]
