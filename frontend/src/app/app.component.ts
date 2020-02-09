import { Component } from '@angular/core';
import {RestService} from './service/rest.service'
import {entity} from './entity/entity'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'archgraph-app';

constructor(private rs: RestService){}


  entity : entity[] = [];
  ngOnInit()
  {
        this.rs.view()
        .subscribe
          (
            (response) =>
            {
              this.entity = response[0]["data"];
            },
            (error) =>
            {
              console.log("No Data Found" + error);
            }

          )
  }
}
