import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {Schema} from '../components/Schema';

@Injectable({
  providedIn: 'root'
})
export class MyServiceService {
  baseUrl = 'http://localhost:5000/';

  getDataNode(type: string, uid: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + type + '/' + uid);
  }

  getSchemaNode(type: string, uid: string): Observable<Schema> {
    return this.http.get<Schema>(this.baseUrl + 'schema' + '/' + type + '/' + uid);
  }

  constructor(private http: HttpClient) {
  }
}
