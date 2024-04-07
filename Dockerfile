FROM python:3.11.9-alpine3.1

WORKDIR app/

COPY . .

RUN pip install pandas
RUN pip install fastapi
RUN pip install pydantic
RUN pip install scikit-learn

EXPOSE 8000

RUN ["uvicorn","modelnew:app"]