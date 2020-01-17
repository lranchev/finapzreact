import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import he from 'he'
import Chart from './Components/Chart';





class App extends Component {
    constructor(){
    super();
    this.state = {
        chartData:{}
     }
    }

    componentWillMount(){
        this.getChartData();
    }

    getChartData(){
        this.setState({
        chartData:{
           labels: ['test1','test2','test3','test4'],
           datasets:[
            {
            label:'Closing price',
            data:[93.93, 95.12, 95.82, 95.31],
            backgroundColor:[
            'rgba(255, 99, 132, 0.6)'
             ]
             }
           ]
         }
        });
    }

 render () {
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

        <Chart chartData={this.state.chartData} location="Akamai" legendPosition='right'/>
      </header>
    </div>
  );

  }
}

export default App;