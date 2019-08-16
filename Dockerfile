FROM python:3.6.6-alpine
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["Deck_Of_Cards.py"]
