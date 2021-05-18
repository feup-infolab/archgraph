import {Injectable} from '@angular/core';
import {BehaviorSubject, Observable} from 'rxjs';
import {HttpClient, HttpParams} from '@angular/common/http';
import {Router} from '@angular/router';
import {User} from '../models';

@Injectable({
  providedIn: 'root'
})
export class FusekiService {
  baseUrl = 'http://localhost:8080';
  private userSubject: BehaviorSubject<User>;
  public user: Observable<User>;

  constructor(private router: Router,
              private http: HttpClient
  ) {
    const user: any = localStorage.getItem('user');
    this.userSubject = new BehaviorSubject<User>(JSON.parse(user));
    this.user = this.userSubject.asObservable();
  }

  getDocById(id: any): Observable<any> {
    const params = new HttpParams()
      .set('id', id);

    return this.http.get(`${this.baseUrl}/doc`, {params});
  }

  getDocSummary(searchObject: any): Observable<any> {
    console.log(searchObject);
    // const params = new HttpParams()
    //   .set('refcode', searchObject.refCode);
    // // .set('query', searchObject);
    // return this.http.get(`${this.baseUrl}/searchdoc`, {params});

    return this.http.post<any>(`${this.baseUrl}/search`, searchObject);
  }

  getDescriptionLevels(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/levelsdesc`);
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


  createDoc(form: any): Observable<any> {
    console.log(form);
    return this.http.post<any>(`${this.baseUrl}/insert`, form);
  }

  updateDoc(form: any, id: any): Observable<any> {
    const params = new HttpParams()
      .set('id', id);
    return this.http.put<any>(`${this.baseUrl}/updatedoc/${id}`, form);
  }
  deleteDoc(id: any): Observable<any> {
    const params = new HttpParams()
      .set('id', id);
    return this.http.delete<any>(`${this.baseUrl}/deletedoc/${id}`);
  }
}

