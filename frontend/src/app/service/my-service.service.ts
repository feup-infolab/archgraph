import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {Example} from '../components/example';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MyServiceService {
  private url: "string";

  getHeroes(): Observable<Example[]> {
    return this.http.get<Example[]>(this.url);
  }

  constructor(private http: HttpClient) {
    this.url
  }
}
