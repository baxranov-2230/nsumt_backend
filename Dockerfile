FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]