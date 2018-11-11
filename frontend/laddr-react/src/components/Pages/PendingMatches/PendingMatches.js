import React, { Component } from "react";
import Page from "../Page";
import PageContent from "../PageContent";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import PendingTabPanels from "./PendingTabPanels";

class PendingMatches extends Component {
  state = {
    received: [1, 2, 3],
    sent: [4, 5, 6]
  };
  render() {
    return (
      <Page title="Pending Matches" subtitle="showing your pending matches">
        <PageContent>
          <Tabs>
            <TabList>
              <Tab>Received</Tab>
              <Tab>Sent</Tab>
            </TabList>
            <TabPanel>
              <PendingTabPanels matches={this.state.received} />
            </TabPanel>
            <TabPanel>
              <PendingTabPanels matches={this.state.sent} />
            </TabPanel>
          </Tabs>
        </PageContent>
      </Page>
    );
  }
}

export default PendingMatches;
