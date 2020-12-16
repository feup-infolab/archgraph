import { Component, OnInit } from '@angular/core';
import {MyService} from "../../service/my.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-person',
  templateUrl: './person.component.html',
  styleUrls: ['./person.component.css']
})
export class PersonComponent implements OnInit {

  private id: any;

  constructor(
      private service: MyService,
      private route: ActivatedRoute,
  ) {
    // this.titles = [];
    // this.notes = [];
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
      // this.getNotes(this.id);
      // this.getSuppliedTitle(this.id);
    });
  }

}
