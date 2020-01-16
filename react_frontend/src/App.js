import React from 'react';
import logo from './logo.svg';
import './App.css';
import he from 'he'





function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>

       <p>The last 4 dates pulled from the API are as follows: {he.decode(window.token)}</p>
       <p>The last 4 closing prices pulled from the API are as follows: {he.decode(window.token2)}</p>

       <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          test  React
        </a>

      <a
          className="App-link"
          href="https://cnbc.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          Check the latest business news
        </a>
      </header>
    </div>
  );
}

export default App;