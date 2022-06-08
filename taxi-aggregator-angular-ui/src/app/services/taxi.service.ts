import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Taxis} from '../model/taxi';
import {URL, TAXI_END_POINT} from '../const/UrlConst';

@Injectable({
  providedIn: 'root'
})
export class TaxiService {

  readonly TAXI_ENDPOINT = URL + TAXI_END_POINT;

  constructor(private httpClient: HttpClient) { }

  public getTaxis(): Observable<Taxis>{
    return this.httpClient.get<Taxis>(this.TAXI_ENDPOINT);
  }
}
