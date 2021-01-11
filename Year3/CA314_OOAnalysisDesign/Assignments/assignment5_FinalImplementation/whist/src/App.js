import React from 'react';
import logo from './logo.svg';
import './App.css';
import socketIOClient from "socket.io-client";
import confetti from 'canvas-confetti';

const ENDPOINT = "http://localhost:8000";
let socket;

class Player extends React.Component {
  render() {
    let name = ""
    switch(this.props.orientation) {
      case "top":
        name = "Partner"
        break;
      default:
      case "bottom":
        name = "You";
        break;
      case "left":
        name = "Opponent 1";
        break;
      case "right":
        name = "Opponent 2";
    }
    let {player} = this.props;
    if(player.state == "GONE") {
      return null
    }
    let card = "TS"
    if(player.card) {
      card = player.card
    }
    if(player.state == "PLAY") {
      card = "1B"
    }
    if(player.state == "WAIT") {
      card = "empty"
    }
    return <div className={"player-" + this.props.orientation}>
      <div className="player">
      <Card of={card}/>
      <div className="player-name">
        {name}
      </div>
      </div>
    </div>
  }
}

class Card extends React.Component {
  render() {
    return <img {...this.props} className="card" src={"/cards/" + this.props.of + ".svg"} />
  }
}
class Cards extends React.Component {
  render() {
    if(!this.props.cards) {
      return null
    }
    return this.props.cards.map((card, index) => {
      let len = this.props.cards.length;
      let proportion = (index + 0.5) / len;
      let rotation = -10 + 20 * proportion;
      let margin = Math.abs(20 * ((index + 0.5) - (0.5 * len)));
      return <div className="card-clickable" style={
        {"transform": `rotate(${rotation}deg)`,
      "margin-top": `${margin}px`}
        }>
        <Card of={card} onClick={() => {this.props.playCard(index)}}/>
      </div>
    })
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { loading: true };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    socket = socketIOClient(ENDPOINT);
    socket.on("connect", () => {
      socket.emit("join game")
    })
    socket.on("reconnect please", () => {
      socket.emit("join game")
    })
    socket.on("welcome", (player_id) => {
      this.setState({player_id})
    })
    socket.on("update_data", data => {
      console.log(data)
      if(this.state.data && this.state.data.game_state == "STARTED" && data.game_state == "FINISHED" && data.teams[data.players[this.state.player_id].team_id].has_won) {
        throwConfetti()
      }
      this.setState({data, loading: false})
    });
  }

  render() {
    if(this.state.loading) {
      return null
    }
    let {data, player_id} = this.state
    let {players, teams, game_state, playerCount} = data
    if(players[player_id] == undefined) {
      return null
    }

    let thisTeamScore = teams[players[player_id].team_id].score
    let otherTeamScore = teams[teams[players[player_id].team_id].enemy_team].score
    let header = null;
    if(game_state == "WAITING") {
      header = <div className="header">
      {playerCount}/4 Players Connected. Share this link with your friends!
    </div>
    }
    if(game_state == "STARTED") {
      header = <div className="header">
          Your Team {thisTeamScore} - {otherTeamScore} Opponent Team
        </div>
    }
    if(game_state == "FINISHED") {
      header = teams[players[player_id].team_id].has_won ? <div className="header header-win">
          Your team has won!
        </div> : <div className="header header-lost">
          You've lost this round :(
        </div>
    }
    return (
      <div className="game">
        {header}
        {this.getPlayers()}
        <div className={`footer ${players[player_id].state != "PLAY" ? "footer-withdrawn" : ""}`}>
          <Cards cards={players[player_id].deck} playCard={this.playCard.bind(this)}/>
        </div>
      </div>
    );
  }

  playCard(card_index) {
    let {data, player_id} = this.state
    let {players, teams} = data
    if(players[player_id].state != "PLAY") {
      return
    }
    socket.emit("play card", {card_index, player_id})
  }

  getPlayers() {
    let bottom = this.state.player_id;
    let top = 1;
    let left = 1;
    let right = 1;
    if (bottom == 1) {
      top = 3;
      left = 2;
      right = 4;
    } else if (bottom == 2) {
      top = 4;
      left = 3;
      right = 1;
    } else if (bottom == 3) {
      top = 1;
      left = 4;
      right = 2;
    } else if (bottom = 4) {
      top = 2;
      left = 1;
      right = 3;
    }
    let { data } = this.state;
    let {players} = data;
    top = players[top];
    left = players[left];
    right = players[right];
    bottom = players[bottom];
    return (
      <>
        <Player orientation="top" player={top} />
        <Player orientation="left" player={left} />
        <Player orientation="right" player={right} />
        <Player orientation="bottom" player={bottom} />
      </>
    )
  }

  handleChange(e) {
    this.setState({ text: e.target.value });
  }

  handleSubmit(e) {
    e.preventDefault();
    if (this.state.text.length === 0) {
      return;
    }
    const newItem = {
      text: this.state.text,
      id: Date.now()
    };
    this.setState(state => ({
      items: state.items.concat(newItem),
      text: ''
    }));
  }
}

export default App;


function throwConfetti() {
  var end = Date.now() + (5 * 1000);
  var colors = ['#2ECC40', '#39CCCC', '#0074D9'];

  (function frame() {
    confetti({
      particleCount: 2,
      angle: 60,
      spread: 55,
      origin: { x: 0 },
      colors: colors
    });
    confetti({
      particleCount: 2,
      angle: 120,
      spread: 55,
      origin: { x: 1 },
      colors: colors
    });

    if (Date.now() < end) {
      requestAnimationFrame(frame);
    }
  }());
}