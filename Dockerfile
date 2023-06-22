# Stage 1: Install dependencies
FROM python:3.10 AS builder

WORKDIR /app

python -m venv venv
. venv/bin/activate

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Stage 2: Copy application code and configure Streamlit
FROM python:3.10

EXPOSE 8599

WORKDIR /app

COPY --from=builder /app/venv /app/venv
. venv/bin/activate/

COPY . .

RUN sed -i 's/\(runOnSave =\).*/\1 false/' .streamlit/config.toml

CMD ["streamlit", "run", "app.py"]

