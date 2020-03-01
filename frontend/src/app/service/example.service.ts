import { Injectable } from '@angular/core';
import {HttpClient, HttpInterceptor} from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import {Observable} from 'rxjs';
import {Example} from '../components/example';
// @ts-ignore
import { HttpErrorHandler, HandleError } from '../http-error-handler.service';
import {catchError} from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    Authorization: 'my-auth-token'
  })
};

@Injectable({
  providedIn: 'root'
})
export class ExampleService {
  Url = 'http://localhost:7474/create';  // URL to public api
  private handleError: HandleError;

  constructor(private http: HttpClient) {
  }

  sendExample(id: Example): Observable<Example> {
    return this.http.get<Example>(this.Url, httpOptions);
  }
}
