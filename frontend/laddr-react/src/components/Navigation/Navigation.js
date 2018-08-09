import React from 'react';
import {NavLink} from "react-router-dom";
import "./Navigation.css";

const Navigation = () => {
    return (
        <nav className="navbar">
            <NavLink to="/">Home</NavLink>
            <NavLink to="/Teams">Teams</NavLink>
            <NavLink to="/Profile">Profile</NavLink>
            <input type="search" name="searchbar" id="searchbar" placeholder="search for a team"/>
        </nav>
    )
}

export default Navigation