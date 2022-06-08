import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Customers} from '../model/user';
import {TAXI_END_POINT, URL, USER_END_POINT} from '../const/UrlConst';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  readonly USERS_ENDPOINT = URL + USER_END_POINT;

  constructor(private httpClient: HttpClient) { }

  public getUsers(): Observable<Customers>{
    return this.httpClient.get<Customers>(this.USERS_ENDPOINT);
  }


}
