import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class Nav extends Component {
  render() {
    return (
      <nav className="nav">
        <div className="nav__logo_area">Laddr</div>
        <ul className="nav__list">
          <li className="nav__list__item">
            <span>[]</span>
            <Link to="/home" className="nav__list__link">
              Home
            </Link>
          </li>
          <li className="nav__list__item">
            <span>[]</span>
            <Link to="/find-players" className="nav__list__link">
              Find players
            </Link>
          </li>
          <li className="nav__list__item">
            <span>[]</span>
            <Link to="/pending-matches" className="nav__list__link">
              Pending matches
            </Link>
          </li>
          <li className="nav__list__item">
            <span>[]</span>
            <Link to="/teams" className="nav__list__link">
              Teams
            </Link>
          </li>
        </ul>
        <div className="nav__profile_area">
          <span className="avatar__pic">[]</span>
          <span className="avatar__name">
            <Link to="/teams" className="nav__list__link">
              {this.props.username}
            </Link>
          </span>
        </div>
      </nav>
    );
  }
}

export default Nav;
