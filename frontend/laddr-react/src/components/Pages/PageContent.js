import React, { Component } from "react";

class PageContent extends Component {
  render() {
    return <div className="page__content">{this.props.children}</div>;
  }
}

export default PageContent;
