import React, { Component } from "react";

class PlayerCard extends Component {
  render() {
    return (
      <div className="matches__card">
        <div className="matches__card__avatar" />
        <div className="matches__card__endorsements" />
        <h2 className="matches__card__name">{this.props.username}</h2>
        <div className="matches__card__info">
          <ul className="matches__card__attributes">
            <li className="matches__card__attribute">{this.props.rank}</li>
            <li className="matches__card__attribute">{this.props.role}</li>
            <li className="matches__card__attribute">{this.props.region}</li>
            <li className="matches__card__attribute">{this.props.language}</li>
            <li className="matches__card__attribute">{this.props.goal}</li>
          </ul>
        </div>
        <div className="matches__card__cta">
          <button className="btn--primary">Select {this.props.username}</button>
        </div>
      </div>
    );
  }
}

export default PlayerCard;
