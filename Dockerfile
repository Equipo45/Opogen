#docker run -p 8501:8501 -e OPEN_AI_KEY="your_open_ai_key" -e PASSWORD="your_password" my-streamlit-app
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pdm

RUN pdm install

EXPOSE 8501

CMD ["pdm", "run", "streamlit", "run", "src/server/main.py"]