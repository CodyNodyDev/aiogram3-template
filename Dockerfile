FROM python:3.10.12
# set work directory
WORKDIR /src/
# copy project
COPY . /src/
# install dependencies
RUN pip install -r requirements.txt
# run app
CMD ["python", "src/main.py"]