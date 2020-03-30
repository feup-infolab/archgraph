import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {Schema} from '../components/Schema';

@Injectable({
  providedIn: 'root'
})
export class MyServiceService {
  baseUrl = 'http://localhost:5000/';

  getDataNode( uid: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + uid);
  }

  getSearchJson( search: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'search' + '/' + search);
  }

  getSchemaNode(uid: string): Observable<Schema> {
    return this.http.get<Schema>(this.baseUrl + 'schema' + '/' + uid);
  }

  sendNode(data): Observable<any> {
    return this.http.post<any>(this.baseUrl + data.uid,  data);
  }

  constructor(private http: HttpClient) {
  }
}
