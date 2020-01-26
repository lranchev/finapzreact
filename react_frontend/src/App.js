import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import he from 'he'
import Chart from './Components/Chart';
import CustomizedRadios from './Components/Radiobutton';

function App() {
  const [radioButtonValue, setRadioButtonValue] = React.useState('amazon');

  function fetchDataFromFlas(event) {
    setRadioButtonValue(event.target.value);
    if(radioButtonValue === "amazon") {
      //todo fetch data for amazon
      console.log('amazon');
    } else {
      //todo data for akamai
      console.log('akamai');
    }
  }


 
  return (
    <div className="App">
      <header className="App-header">


       <CustomizedRadios fetchDataFromFlas={fetchDataFromFlas} />
       <Chart chart_label={window.chart1} chart_data={window.chart2} chart_title="Test Amazon Stock" />

      {/*<p>The last 10 dates pulled from the API are as follows: {he.decode(window.chart1)}</p>*/}
      {/*<p>The last 10 closing prices pulled from the API are as follows: {he.decode(window.chart2)}</p>*/}

       <Chart chart_label={window.chart3} chart_data={window.chart4} chart_title="Test Akamai Stock"/>

       {/*<p>The last 10 dates pulled from the API are as follows: {he.decode(window.chart3)}</p>*/}
       {/*<p>The last 10 closing prices pulled from the API are as follows: {he.decode(window.chart4)}</p>*/}

        <img src={logo} className="App-logo" alt="logo" />




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