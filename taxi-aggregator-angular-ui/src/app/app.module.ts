import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SideNavComponent } from './side-nav/side-nav.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavigationComponent } from './navigation/navigation.component';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import {MatIconModule, MatIconRegistry} from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatCardModule } from '@angular/material/card';
import { MatMenuModule } from '@angular/material/menu';
import { CardComponent } from './card/card.component';
import {HighchartsChartModule} from 'highcharts-angular';
import { LocationchartComponent } from './locationchart/locationchart.component';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import { UserdatagridComponent } from './userdatagrid/userdatagrid.component';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { TaxidatagridComponent } from './taxidatagrid/taxidatagrid.component'

@NgModule({
  declarations: [
    AppComponent,
    SideNavComponent,
    NavigationComponent,
    DashboardComponent,
    CardComponent,
    LocationchartComponent,
    UserdatagridComponent,
    TaxidatagridComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    LayoutModule,
    MatToolbarModule,
    MatButtonModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatGridListModule,
    MatCardModule,
    MatMenuModule,
    HighchartsChartModule,
    HttpClientModule,
    MatTableModule,
    MatPaginatorModule
  ],
  providers: [HttpClient, MatIconRegistry],
  bootstrap: [AppComponent]
})
export class AppModule { }
