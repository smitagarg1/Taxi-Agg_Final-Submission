import { Component, OnInit } from '@angular/core';
import * as Highcharts from 'highcharts';
import {TaxiService} from '../services/taxi.service';
import {Taxis} from '../model/taxi';
import {forkJoin, timer} from 'rxjs';
import {UsersService} from '../services/users.service';

@Component({
  selector: 'app-locationchart',
  templateUrl: './locationchart.component.html',
  styleUrls: ['./locationchart.component.scss']
})
export class LocationchartComponent implements OnInit{

  Highcharts: typeof Highcharts = Highcharts;
  chartOptions: Highcharts.Options;

  userData = [];
  taxiData = [];

  value = 0;

  constructor(private taxiService: TaxiService, private userService: UsersService) {
  }

  ngOnInit(): void {
    this.loadChart();
    setInterval(() => {
      this.loadChart();
      this.startTimer();
    },  30000);
  }

  startTimer() {
    this.value = 0;
    setInterval(() => {
      this.value += 1;
    }, 1000);
  }

  loadChart() {
    this.userData = [];
    this.taxiData = [];
    forkJoin([this.taxiService.getTaxis(), this.userService.getUsers()])
      .subscribe((responses) => {
        responses[0].taxiList.forEach(taxi => {
          this.taxiData.push(taxi.location.coordinates);
        });
        responses[1].customerList.forEach(taxi => {
          this.userData.push(taxi.location.coordinates);
        });
        this.initChart();
      }, error => {
        console.log(error);
      });
  }

  initChart(): void {
    this.chartOptions = {
      chart: {
        type: 'scatter',
        zoomType: 'xy',
      },
      title: {
        text: 'Location of Taxis and users'
      },
      xAxis: {
        title: {
          text: 'Longitude'
        },
        startOnTick: true,
        endOnTick: true,
        showLastLabel: true
      },
      yAxis: {
        title: {
          text: 'Latitude'
        }
      },
      legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 100,
        y: 0,
        floating: true,
        backgroundColor: Highcharts.defaultOptions.chart.backgroundColor,
        borderWidth: 1
      },
      plotOptions: {
        scatter: {
          marker: {
            radius: 5,
            states: {
              hover: {
                enabled: true,
                lineColor: 'rgb(100,100,100)'
              }
            }
          },
          states: {
            hover: {}
          },
          tooltip: {
            headerFormat: '<b>{series.name}</b><br>',
            pointFormat: '{point.x} °, {point.y} °'
          }
        }
      },
      series: [{
        name: 'Taxis',
        color: 'rgba(223, 83, 83, .9)',
        type: 'scatter',
        data: this.taxiData

      }, {
        name: 'Users',
        color: 'rgba(119, 152, 191, .9)',
        type: 'scatter',
        data: this.userData
      }]
    };
  }
}
