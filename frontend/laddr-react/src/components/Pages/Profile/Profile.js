import React, { Component } from "react";
import Page from "../Page";
import PageContent from "../PageContent";

class Profile extends Component {
  render() {
    return (
      <Page title="Profile" subtitle="showing a profile">
        <PageContent>test</PageContent>
      </Page>
    );
  }
}

export default Profile;
