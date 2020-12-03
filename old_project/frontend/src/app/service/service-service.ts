import {Injectable} from '@angular/core';
import {Observable, Subject} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';
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

  getDataNode(uid: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + uid);
  }

  getDataNodeWithTemplate(uid: string, template: object): Observable<any[]> {
    return this.http.post<any[]>(this.baseUrl + 'withtemplate/' + uid, template);
  }

  getBaseDataNodeWithTemplate(uid: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'withtemplate/' + uid);
  }

  getTemplatesFromEntity(uid: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'templatesfromentity/' + uid);
  }


  getSearchJson(search: string): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'search/' + search);
  }

  getSpecificSearchJson(entity: string, search: string): Observable<any[]> {
    if (search === '') {
      return this.http.get<any[]>(this.baseUrl + 'search_specific/' + entity);
    } else {
      return this.http.get<any[]>(this.baseUrl + 'search_specific/' + entity + '/' + search);
    }
  }

  getSchemaNode(uid: string): Observable<Schema> {
    return this.http.get<Schema>(this.baseUrl + 'schema/' + uid);
  }

  getSchemaNodeWithTemplate(uid: string, template: object): Observable<Schema> {
    // const headers = new HttpHeaders();
    // headers.append('template', template)
    return this.http.post<Schema>(this.baseUrl + 'schemawithtemplate/' + uid, template);
  }

  getBaseSchemaNodeWithTemplate(uid: string): Observable<Schema> {
    return this.http.get<Schema>(this.baseUrl + 'template/' + uid);
  }

  geAllSchemaProperties(uid: string): Observable<Schema> {
    return this.http.get<Schema>(this.baseUrl + 'getallproperties/' + uid);
  }

  getTemplate(): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + 'obtainschema');
  }

  sendNode(data, template): Observable<any> {
    const uid = Object.keys(data)[0];
    const body = {
      template,
      data: data[uid]
    };

    return this.http.post<any>(this.baseUrl + uid, body);
  }

  sendTemplate(uid, template): Observable<any> {
    return this.http.post<any>(this.baseUrl + 'inserttemplate/' + uid, template);
  }

  postTemplate(template): Observable<any> {
    return this.http.post<any>(this.baseUrl + 'post_template', template);
  }

  getDocTemplate(uid): Observable<any> {
    return this.http.get<any>(this.baseUrl + 'uidglab/' + uid);
  }

  postDocTemplate(uid, content): Observable<any> {
    return this.http.post<any>(this.baseUrl + 'uidglab/' + uid, content);
  }

  getAllTitleTypes(): Observable<any> {
    return this.http.get<any>(this.baseUrl + 'control_values/title_types');
  }

  getAllIdentifierTypes(): Observable<any> {
    return this.http.get<any>(this.baseUrl + 'control_values/identifier_types');
  }

  constructor(private http: HttpClient) {

    this.shareMethod$ = this.shareMethodSubject.asObservable();
  }

}
