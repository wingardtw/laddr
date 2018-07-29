import React, { Component } from 'react';
import Navbar from './components/navbar.js';
import Alert from './components/alert.js';
import Dashboard from './components/dashboard.js';
import './css/App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
{/* BEGIN HEADER with logo and navbar */}
        <header className="App-header">
          <Navbar />
          <h1 className="App-title">Home</h1>
        </header>

{/* this is going to be the home page with dashboard view */}
        <main className="main">
        <Alert alertMessage="this is an alert" />
        <Dashboard />
        </main>
      </div>
    );
  }
}

export default App;
