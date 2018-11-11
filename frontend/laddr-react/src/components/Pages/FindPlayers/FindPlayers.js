import React, { Component } from "react";
import Page from "../Page";
import PageContent from "../PageContent";
import PlayerCard from "./PlayerCard";

const players = [
  {
    id: 1,
    username: "Lorem",
    rank: "Gold IV",
    role: "top",
    region: "NA",
    language: "EN",
    goal: "this is a story all about how"
  },
  {
    id: 2,
    username: "Ipsum",
    rank: "Gold IV",
    role: "top",
    region: "NA",
    language: "EN",
    goal: "this is a story all about how"
  },
  {
    id: 3,
    username: "Dolor",
    rank: "Gold IV",
    role: "top",
    region: "NA",
    language: "EN",
    goal: "this is a story all about how"
  }
];

const listPlayers = players.map(player => (
  <PlayerCard
    key={player.id}
    username={player.username}
    rank={player.rank}
    role={player.role}
    region={player.region}
    language={player.language}
    goal={player.goal}
  />
));

class FindPlayers extends Component {
  render() {
    return (
      <Page title="Find Players" subtitle="Showing curated matches">
        <PageContent>
          <div className="matches__attributes">
            <div className="matches__card__info">
              <ul className="matches__card__attributes matches__card__attributes--side">
                <li className="matches__card__attribute">Rank</li>
                <li className="matches__card__attribute">Role</li>
                <li className="matches__card__attribute">Region</li>
                <li className="matches__card__attribute">Language</li>
                <li className="matches__card__attribute">Goal</li>
              </ul>
            </div>
          </div>
          <div className="matches__container">{listPlayers}</div>
        </PageContent>
      </Page>
    );
  }
}

export default FindPlayers;
