import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link, NavLink, Redirect} from "react-router-dom";

class Navbar extends Component {
    render() {
        return (
            <ul className="navbar">
                <li className="navbar__item">
                    <NavLink to="/" exact className="navbar__link" activeClassName="nav__link--active">Home</NavLink>
                </li>
                <li className="navbar__item">
                    <NavLink to="/Teams"  exact className="navbar__link" activeClassName="nav__link--active">Teams</NavLink>
                </li>
                <li className="navbar__item">
                    <NavLink to="/Matches"  exact className="navbar__link" activeClassName="nav__link--active">Matches</NavLink>
                </li>
                <li className="navbar__item">
                    <NavLink to="/Profile"  exact className="navbar__link" activeClassName="nav__link--active">Profile</NavLink>
                </li>
            </ul>
        )
    }
}

export default Navbar;