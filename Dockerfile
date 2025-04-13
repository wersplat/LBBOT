FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python", "src/dashboard/app.py"]