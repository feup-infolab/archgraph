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
  public Name: any;
  public Identifier: any;
  public Location: any;
  public AdminDivision: any;
  public Latitude: any;
  public Longitude: any;
  public Keywords: any;
  public RelatedTo: any;

  constructor(
      private service: MyService,
      private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      // this.id = params.get('id');
      this.getPlaceSummary(this.Identifier);
      // this.getAllDocById(this.id);
    });
  }

  getPlaceSummary(Identifier: any) {
    this.service.getPlaceSummary(Identifier)
        .subscribe(result => {
          console.log(result);
          // this.identifiers = result.results.bindings;
        });
  }
}

