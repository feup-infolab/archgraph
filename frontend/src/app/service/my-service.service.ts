import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {Example} from '../components/example';
import {HttpClient} from '@angular/common/http';
import {map} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class MyServiceService {

  getExample(): Observable<Example[]> {
    return this.http.get<any[]>('http://localhost:5000/string/5d5a3be2e8624ad180478d1a75c6fd13')
      .pipe(map(data => data));
  }

  constructor(private http: HttpClient) {
  }
}
