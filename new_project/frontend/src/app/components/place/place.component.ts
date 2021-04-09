import { Component, OnInit } from '@angular/core';
import {FusekiService} from '../../service/fuseki.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-place',
  templateUrl: './place.component.html',
  styleUrls: ['./place.component.css', '../default.css']
})
export class PlaceComponent implements OnInit {

  private id: any;

  constructor(
      private service: FusekiService,
      private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
      // this.getNotes(this.id);
      // this.getSuppliedTitle(this.id);
    });
  }
}
