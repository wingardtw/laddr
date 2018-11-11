import React, { Component } from "react";

class Searchbar extends Component {
  render() {
    return (
      <span className="page__searchbar">
        <input
          type="search"
          name="search"
          id=""
          className="searchbar"
          placeholder="search"
        />
      </span>
    );
  }
}

export default Searchbar;
