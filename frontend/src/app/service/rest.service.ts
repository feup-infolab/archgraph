import { Injectable, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {entity} from '../entity/entity';

@Injectable({
  providedIn: 'root'
})

export class RestService implements OnInit {

  constructor(private http : HttpClient ) {
  }

  ngOnInit(){
  }

  Url : string = "http://127.0.0.1:5000/";

  view()
  {
      return this.http.get<entity[]>(this.Url);
  }
}

