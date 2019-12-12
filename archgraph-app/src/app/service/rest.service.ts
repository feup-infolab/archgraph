import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class RestService implements OnInit {

  constructor(private http : HttpClient ) { }
}

weatherUrl : string = "http://127.0.0.1:5000/";

view()
{
    return this.http.get<Weather[]>(this.weatherUrl);
}
