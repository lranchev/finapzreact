import React, {Component} from 'react';
import {Bar, Line, Pie} from 'react-chartjs-2';

class Chart extends Component{
  constructor(props){
    super(props);
    this.state = {
     chartData:props.chartData
    }
  }

  static defaultProps = {
    displayTitle:true,
    displayLegend:true,
    legendPosition:'right',
    location:'City_stock'
  }
    render (){
         return (
            <div className="chart">


                <Line
                  data={this.state.chartData}
                  width={900}
                  height={400}
                  options={{
                    title:{
                        display:this.props.displayTitle,
                        text:'Akamai Stock',
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