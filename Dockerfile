FROM python:3.11-bookworm

WORKDIR /workdir

COPY requirements.txt /workdir
RUN pip install -r requirements.txt

COPY app.py /workdir
COPY assets /workdir/assets

EXPOSE 8080

ENTRYPOINT ["gunicorn", "main:server", "-b", ":8080"]