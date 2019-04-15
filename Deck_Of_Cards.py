from Deck import Deck
from flask import Flask

final_cards=""
deck = Deck()
app = Flask(__name__)

@app.route("/deal")
def deal():
    deck.deal()
    return 'Deck is ready'

@app.route("/shuffle")
def shuffle():
    if len(deck.cards) > 0:
        deck.shuffle()
        return 'Deck is shuffled'
    else:
        return 'No cards to shuffle'

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
   app.run(host='0.0.0.0', port=5000, debug=True)


