import { Injectable } from '@angular/core';
import {Observable, Subject} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {Schema} from '../models/Schema';

@Injectable({
  providedIn: 'root'
})
export class MyServiceService {
  baseUrl = 'http://localhost:5000/';
  shareMethod$: Observable<any>;
  private shareMethodSubject = new Subject<any>();


  shareMethod(data: string) {
    this.shareMethodSubject.next(data);
  }

  getDataNode( uid: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + uid);
  }

  getDataNodeWithTemplate( uid: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'withtemplate/' + uid);
  }

  getBaseDataNodeWithTemplate( uid: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'createwithtemplate/' + uid);
  }


  getSearchJson( search: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'search' + '/' + search);
  }

  getSpecificSearchJson(entity: string, search: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'search_specific' + '/' + entity + '/' + search);
  }

  getSchemaNode(uid: string): Observable<Schema> {
    return this.http.get<Schema>(this.baseUrl + 'schema' + '/' + uid);
  }

  getSchemaNodeWithTemplate(uid: string): Observable<Schema> {
    return this.http.get<Schema>(this.baseUrl + 'schemawithtemplate' + '/' + uid);
  }

  getBaseSchemaNodeWithTemplate(uid: string): Observable<Schema> {
    return this.http.get<Schema>(this.baseUrl + 'createtemplate' + '/' + uid);
  }

  geAllSchemaProperties(uid: string): Observable<Schema> {
    return this.http.get<Schema>(this.baseUrl + 'getallproperties' + '/' + uid);
  }

  getTemplate(): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'obtainschema');
  }

  sendNode(data): Observable<any> {
    const uid = Object.keys(data)[0];
    return this.http.post<any>(this.baseUrl + uid,  data[uid]);
  }

  sendTemplate(data): Observable<any> {
    return this.http.post<any>(this.baseUrl + 'post_template', data);
  }

  constructor(private http: HttpClient) {

    this.shareMethod$ = this.shareMethodSubject.asObservable();
  }

}
