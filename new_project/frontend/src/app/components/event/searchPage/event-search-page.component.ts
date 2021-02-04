import { Component, OnInit } from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-event-search-page',
  templateUrl: './event-search-page.component.html',
  styleUrls: ['./event-search-page.component.css']
})
export class EventSearchPageComponent implements OnInit {
  //  event
  public Name: any;
  public Type: any;
  public Location: any;
  public Address: any;
  public Latitude: any;
  public Longitude: any;
  public Keywords: any;
  public RelatedTo: any;
  public CulturalPeriod: any;
  public EndDateTo: any;
  public EndDateFrom: any;
  public StartDateFrom: any;
  public Identifier: any;
  public StartDateTo: any;

  constructor(
      private service: MyService,
      private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      // this.id = params.get('id');
      this.getEventSummary(this.Identifier);
      // this.getAllDocById(this.id);
    });
  }

  getEventSummary(Identifier: any) {
    this.service.getEventSummary(Identifier)
        .subscribe(result => {
          console.log(result);
          // this.identifiers = result.results.bindings;
        });
  }
}
