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
  Url = 'http://localhost:3000/';  // URL to web api
  private handleError: HandleError;

  constructor(private http: HttpClient) {
  }

  sendExample(example: Example): Observable<Example> {
    return this.http.post<Example>(this.Url, example, httpOptions);
  }
}
