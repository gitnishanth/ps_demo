FROM python:3.5
RUN pip3 install Flask
RUN pip3 install requests
RUN useradd -ms /bin/bash admin
USER admin
WORKDIR /app
COPY app /app
CMD ["python3", "PSAPI.py"]
