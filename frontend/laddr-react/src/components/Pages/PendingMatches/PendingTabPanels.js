import React, { Component } from "react";
import PlayerCard from "../FindPlayers/PlayerCard";

class PendingTabPanels extends Component {
  renderMatches() {
    if (this.props.matches.length === 0) return <p>There are no matches!</p>;
    return (
      <ul>
        {this.props.matches.map(match => (
          <li key={match}>{match}</li>
        ))}
      </ul>
    );
  }

  render() {
    return (
      <div className="pending_tab_panels">
        <div className="pending_tab__entries">{this.renderMatches()}</div>
        <div className="pending_tab__request" />
        <div className="pending_tab__player_card">
          <PlayerCard />
        </div>
      </div>
    );
  }
}

export default PendingTabPanels;
