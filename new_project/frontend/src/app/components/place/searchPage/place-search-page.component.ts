import { Component, OnInit } from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-place-search-page',
  templateUrl: './place-search-page.component.html',
  styleUrls: ['./place-search-page.component.css']
})
export class PlaceSearchPageComponent implements OnInit {
  // place
  public name: any;
  public identifier: any;
  public location: any;
  public adminDivision: any;
  public latitude: any;
  public longitude: any;
  public keywords: any;
  public relatedTo: any;

  constructor(
      private service: MyService,
      private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      // this.id = params.get('id');
      this.getPlaceSummary(this.identifier);
      // this.getAllDocById(this.id);
    });
  }

  getPlaceSummary(identifier: any) {
    this.service.getPlaceSummary(identifier)
        .subscribe(result => {
          console.log(result);
          // this.identifiers = result.results.bindings;
        });
  }
}

