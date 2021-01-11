const express = require('express');
const bodyParser = require('body-parser')
const path = require('path');
const { v4: uuidv4 } = require('uuid');
const socketio = require('socket.io');

var app = express();

var http = require('http').Server(app);

var io = socketio(http, {
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
    allowedHeaders: ["my-custom-header"],
    credentials: true
  }
});
var port = process.env.PORT || 8000;

var games = {
}
let game = {}
let resetGame = () => {
  game = {
    players: {
      1: {
        state: "GONE",
        team_id: 1,
      },
      2: {
        state: "GONE",
        team_id: 2
      },
      3: {
        state: "GONE",
        team_id: 1,
      },
      4: {
        state: "GONE",
        team_id: 2
      }
    },
    teams: {
      1: {
        score: 0,
        enemy_team: 2,
        has_won: false
      },
      2: {
        score: 0,
        enemy_team: 1,
        has_won: false
      }
    },
    card_history: [],
    playerCount: 0,
    playerTurn: 1,
    playerTurnId: 1,
    totalRounds: 0,
    game_state: "WAITING",
  }
}
resetGame()
app.get('/game/:id', function (req, res) {
  return res.sendFile(path.join(__dirname, 'build', 'index.html'));
});
app.get('/', function (req, res) {
  let newId = uuidv4();
  resetGame()
  return res.redirect(`/game/${newId}`)
});

app.use(express.static(path.join(__dirname, 'build')));

let deck = ["2H", "3H", "4S", "6C", "7D", "8H", "9S", "KC", "QD", "TH",
  "3S", "5C", "6D", "7H", "8S", "AC", "JC", "KD", "QH", "TS",
  "2S", "4C", "5D", "6H", "7S", "9C", "AD", "JD", "KH", "QS",
  "2C", "3C", "4D", "5H", "6S", "8C", "9D", "AH", "JH", "KS", "TC",
  "2D", "3D", "4H", "5S", "7C", "8D", "9H", "AS", "JS", "QC", "TD"]

const card_rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

function get_card_details(card) {
  return {
    suite: card[1],
    rank: card[0]
  }
}
io.on('connection', function (socket) {
  let update_players = () => {
    io.emit('update_data', game);
  }
  let next_round = () => {
    for (var i = 0; i < 4; i += 1) {
      game.players[i + 1].state = "WAIT"
      game.players[i + 1].card = null;
    }
    game.card_history = [];
    game.players[game.playerTurnId].state = "PLAY"
    game.playerTurn = 1;
  }
  let judge_round = () => {
    let card_history = game.card_history;
    let leading_suite = card_history[0].card.suite;
    card_history.forEach((card) => (card.relative_rank = card_rank.indexOf(card.card.rank)))
    card_history.forEach((card) => (card.card.suite != leading_suite ? card.relative_rank = -1 : null))
    card_history = card_history.sort((a, b) => b.relative_rank - a.relative_rank)
    let winning_card = card_history[0]
    console.log(card_history)
    console.log("winning card is")
    console.log(winning_card)
    game.teams[game.players[winning_card.player_id].team_id].score += 1
    if(game.players[winning_card.player_id].deck.length == 0) {
      if(game.teams[1].score > game.teams[2].score) {
        game.teams[1].has_won = true
      } else {
        game.teams[2].has_won = true
      }
      finish_game()
      return
    }
    game.playerTurnId = winning_card.player_id
  }
  let start_game = () => {
    shuffle(deck);
    for (var i = 0; i < 4; i += 1) {
      game.players[i + 1].deck = deck.slice(i * 12, (i + 1) * 12);
    }
    game.game_state = "STARTED";
    next_round()
  }
  let finish_game = () => {
    game.game_state = "FINISHED";
    update_players()
    setTimeout(() => {reset_game_state()}, 5000);
  }
  let reset_game_state = () => {
    resetGame()
    io.emit("reconnect please");
  }
  console.log('connection!')
  socket.on('join game', function () {
    if (game.playerCount == 4) {
      return
    }
    let playerid = game.playerCount + 1
    game.playerCount += 1
    game.players[playerid].state = "WAIT"
    socket.emit("welcome", playerid)
    if (game.playerCount == 4) {
      start_game()
    }
    update_players()
  });
  socket.on('play card', function (data) {
    console.log("card played")
    let { player_id, card_index } = data;
    let card = game.players[player_id].deck[card_index];
    game.players[player_id].state = "PLAYED";
    game.players[player_id].card = card;
    game.players[player_id].deck.splice(card_index, 1);
    game.card_history.push({player_id, card: get_card_details(card)})
    game.playerTurn += 1;
    game.playerTurnId += 1;
    game.totalRounds += 1;
    if(game.playerTurnId > 4) {
      game.playerTurnId = 1;
    }
    if(game.totalRounds >= 13) {
      
    }
    if (game.playerTurn > 4) {
      judge_round()
      next_round()
    } else {
      game.players[game.playerTurnId].state = "PLAY";
    }
    update_players()
  });
  socket.on('disconnect', () => {
    reset_game_state()
  })
});

http.listen(port, function () {
  console.log('listening on *:' + port);
});
