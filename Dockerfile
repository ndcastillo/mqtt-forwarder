FROM python:3.8-slim-buster

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY mqtt_forwarder.py /app/mqtt_forwarder.py

ENV MQTT_BROKER mosquitto
ENV MQTT_FORWARDER_TOPIC forwarded/topic
ENV MQTT_REMOTE_BROKER example.com
ENV MQTT_REMOTE_PORT 1883

CMD ["python", "/app/mqtt_forwarder.py"]
