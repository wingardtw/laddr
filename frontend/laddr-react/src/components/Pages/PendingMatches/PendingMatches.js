import React, { Component } from "react";
import Page from "../Page";
import PageContent from "../PageContent";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import PendingTabPanels from "./PendingTabPanels";

class PendingMatches extends Component {
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
              <PendingTabPanels />
            </TabPanel>
            <TabPanel>
              <h2>Sent</h2>
            </TabPanel>
          </Tabs>
        </PageContent>
      </Page>
    );
  }
}

export default PendingMatches;
