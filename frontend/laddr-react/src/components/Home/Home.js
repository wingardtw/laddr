import React, { Component } from 'react';
import "./Home.css"
class Home extends Component {
    render() {
        return (
            <div className="container">
                <aside className="events">
                    <p className="events__title">
                        upcoming events:
                    </p>
                </aside>
                <main className="main">
                    <h1>Home</h1>
                    <div className="dashboard">
                        <div className="dashboard__item dashboard__item--1 dashboard__item--small"></div>
                        <div className="dashboard__item dashboard__item--2 dashboard__item--medium"></div>
                        <div className="dashboard__item dashboard__item--3 dashboard__item--large"></div>
                    </div>
                </main>
                <aside className="aside--2">
                    Aside
                </aside>
            </div>
        )
    }
}

export default Home;