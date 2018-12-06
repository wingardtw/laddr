import React, { Component } from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class App extends Component {
  state = {
    isLoggedIn: false
  };
  handleLogin = () => {
    this.setState(prevState => ({
      isLoggedIn: !prevState.isLoggedIn
    }));
  };
  render() {
    function extendList(e) {
      console.log("this was clicked");
    }
    return (
      <div className="app wrapper">
        <div className="page">
          <header className="header">
            <div className="logo" />
            <div className="search">
              <input
                type="search"
                className="search__bar"
                placeholder="Search"
              />
              <button className="btn search__btn">go</button>
            </div>
          </header>
          <div className="menu">
            <div className="alert">!</div>
            <div className="menu__container" onClick={extendList}>
              <ul className="menu__list">
                <li className="menu__items">Item</li>
                <li className="menu__items">Item</li>
                <li className="menu__items">Item</li>
              </ul>
            </div>
          </div>
          <main className="content">
            <h1 className="content__title">Title </h1>
            <h2 className="content__subtitle">Subtitle</h2>
          </main>
        </div>
        <nav className="nav">
          <ul className="nav__list">
            <li className="nav__item">
              <span className="nav__item__icon" />
              Home
            </li>
            <li className="nav__item">
              <span className="nav__item__icon" />
              Teams
            </li>
            <li className="nav__item">
              <span className="nav__item__icon" />
              Matches
            </li>
            <li className="nav__item">
              <span className="nav__item__icon" />
              Profile
            </li>
          </ul>
        </nav>
      </div>
    );
  }
}

export default App;
