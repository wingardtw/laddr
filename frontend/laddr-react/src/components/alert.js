import React, { Component } from 'react';
import '../css/alert.css';

class Alert extends Component {
    render() {
      return (
        <div className="alert">
            {this.props.alertMessage}
        </div>
      );
    }
  }
  
  export default Alert;