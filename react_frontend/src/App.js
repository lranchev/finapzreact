import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import he from 'he'
import Chart from './Components/Chart';


{/* var token3array = window.token3.join().split('-') */}

function App() {


  return (
    <div className="App">
      <header className="App-header">



       <Chart token3={window.token3} token4={window.token4} />
        <img src={logo} className="App-logo" alt="logo" />

       <p>The last 4 dates pulled from the API are as follows: {he.decode(window.token)}</p>
       <p>Array: The last 4 dates pulled from the API are as follows: {window.token3}</p>
       <p>The last 4 closing prices pulled from the API are as follows: {he.decode(window.token2)}</p>
       <p>Array: The last 4 closing prices pulled from the API are as follows: {window.token4}</p>
{/*       <p>token3array: The last 4 closing prices pulled from the API are as follows: {token3array}</p> */}


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