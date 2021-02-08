import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient, HttpParams} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MyService {
  baseUrl = 'http://localhost:8080';

  constructor(private http: HttpClient) {
  }

  getDocById(id: any): Observable<any> {
    const params = new HttpParams()
      .set('id', id);

    return this.http.get(`${this.baseUrl}/doc`, {params});
  }

  getDocSummary(searchObject: any): Observable<any> {
    console.log(searchObject);
    const params = new HttpParams()
      .set('refcode', searchObject.referenceCode);
    // .set('query', searchObject);
    return this.http.get(`${this.baseUrl}/searchdoc`, {params});
  }

  getActorById(id: any): Observable<any> {
    const params = new HttpParams()
      .set('id', id);
    return this.http.get(`${this.baseUrl}/actor`, {params});
  }

  getActorSummary(searchObject: any): Observable<any> {
    const params = new HttpParams()
      .set('identifier', searchObject.identifier);
    // .set('query', searchObject);


    return this.http.get(`${this.baseUrl}/searchactor`, {params});
  }

  getEventById(id: any): Observable<any> {
    const params = new HttpParams()
      .set('id', id);
    return this.http.get(`${this.baseUrl}/event`, {params});
  }

  getEventSummary(searchObject: any): Observable<any> {
    const params = new HttpParams()
      // .set('identifier', searchObject.identifier);
      .set('query', searchObject);
    return this.http.get(`${this.baseUrl}/searchevent`, {params});
  }

  getOrgById(id: any): Observable<any> {
    const params = new HttpParams()
      .set('id', id);
    return this.http.get(`${this.baseUrl}/org`, {params});
  }

  getOrgSummary(searchObject: any): Observable<any> {
    const params = new HttpParams()
      // .set('identifier', searchObject.identifier);
      .set('query', searchObject);
    return this.http.get(`${this.baseUrl}/searchorg`, {params});
  }

  getPlaceById(id: any): Observable<any> {
    const params = new HttpParams()
      .set('id', id);
    return this.http.get(`${this.baseUrl}/place`, {params});
  }

  getPlaceSummary(searchObject: any): Observable<any> {
    const params = new HttpParams()
      // .set('identifier', searchObject.identifier);
      .set('query', searchObject);
    return this.http.get(`${this.baseUrl}/searchplace`, {params});
  }
}

