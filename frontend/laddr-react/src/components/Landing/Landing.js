import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom"; 

class Landing extends Component {
    render() {
        return (
            <div className="landing__wrapper">
                <h1 className="landing__heading">
                    This is the landing.
                </h1>
                <Link to="/home" className="nav__list__link">Home</Link>
            </div>
        )
    }
}

export default Landing