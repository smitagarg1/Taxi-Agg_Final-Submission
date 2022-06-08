import {Component, Input, OnInit} from '@angular/core';
import {Customer} from '../model/user';
import {UsersService} from '../services/users.service';
import {Taxi} from '../model/taxi';
import {TaxiService} from '../services/taxi.service';

@Component({
  selector: 'app-taxidatagrid',
  templateUrl: './taxidatagrid.component.html',
  styleUrls: ['./taxidatagrid.component.scss']
})
export class TaxidatagridComponent implements OnInit {

  displayedColumns: string[] = ['name', 'location', 'type', 'timestamp'];
  @Input()
  dataSource: Taxi[];
  resultsLength: number;

  constructor(private taxiService: TaxiService) { }

  ngOnInit(): void {
    this.taxiService.getTaxis().subscribe((resp) => {
      this.resultsLength = resp.taxiList.length;
      this.dataSource = resp.taxiList.sort((a, b) => (a.timestamp > b.timestamp) ? 1 : -1);
    });
  }

}
