import React, {Component} from 'react';
import {Bar, Line, Pie} from 'react-chartjs-2';

class Chart extends Component{
  constructor(props){
    super(props);
    this.state = {
     chartData:{
       labels: ['Boston', 'Lowell'],
       datasets:[
        {
        label:'Population',
        data:[617594,181045],
        backgroundColor:[
        'rgba(255, 99, 132, 0.6)',
        'rgba(255, 192, 86, 0.6)'
         ]
         }
       ]
     }
    }
  }

  static defaultProps = {
    displayTitle:true,
    displayLegend:true,
    legendPosition:'right'
  }
    render (){
         return (
            <div className="chart">
                <Bar
                  data={this.state.chartData}
                  width={1000}
                  height={1000}
                  options={{
                    title:{
                        display:this.props.displayTitle,
                        text:'Largest Cities in Mass',
                        fontSize:25
                    },
                    legend:{
                        display:this.props.displayLegend,
                        position:this.props.legendPosition
                    }
                  }}
                />
            </div>
         )
    }

}

export default Chart;