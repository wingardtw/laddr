import React, { Component } from "react";

class PageHeader extends Component {
  render() {
    return (
      <div className="page__header">
        <h1 className="page__title">{this.props.title}</h1>
        <p className="page__subtitle">{this.props.subtitle}</p>
      </div>
    );
  }
}

export default PageHeader;
