import React, { Component } from 'react';
import './css/App.css';
import BasicExample from './components/BasicExample.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <BasicExample />
      </div>
    );
  }
}

export default App;
