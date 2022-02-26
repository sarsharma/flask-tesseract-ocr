FROM python:alpine3.15
RUN apk add tesseract-ocr \
&& apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers zlib-dev jpeg-dev && apk add libjpeg \
&& pip install Pillow --no-cache-dir && apk del .tmp \
&& pip install flask --no-cache-dir
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000
