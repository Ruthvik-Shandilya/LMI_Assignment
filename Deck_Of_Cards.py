from Deck import Deck
from flask import Flask
import os

final_cards=""
deck = Deck()
app = Flask(__name__)

@app.route("/")
def welcome():
    return '<h2>Welcome to the Game of Deck Of Cards</h2>'

@app.route("/deal")
def deal():
    deck.deal()
    return '<h2>Deck is ready</h2>'

@app.route("/shuffle")
def shuffle():
    if len(deck.cards) > 0:
        deck.shuffle()
        return '<h2>Deck is shuffled</h2>'
    else:
        return '<h2>No cards to shuffle</h2>'

@app.route("/drawCards")
def drawCard():
    if len(deck.cards) > 0:
        response = deck.drawCard()
        global final_cards
        final_cards += response.suite + ' : ' + response.rank + "<br>"
        return final_cards
    else:
        return final_cards+'<script>alert("No cards to deal, Please check your existing dealt cards")</script>'

@app.route("/drawOneCard")
def drawOneCard():
    if len(deck.cards) > 0:
        response = deck.drawCard()
        global final_cards
        final_cards += response.suite + ' : ' + response.rank + "<br>"
        return response.suite + ' : ' + response.rank
    else:
        return final_cards+'<script>alert("No cards to deal, Please check your existing dealt cards")</script>'


if __name__ == "__main__":
   port = int(os.environ.get('PORT',5000))
   app.run(host='0.0.0.0', port=port, debug=True)


