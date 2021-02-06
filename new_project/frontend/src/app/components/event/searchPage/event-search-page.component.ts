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
  public name: any;
  public type: any;
  public location: any;
  public address: any;
  public latitude: any;
  public longitude: any;
  public keywords: any;
  public relatedTo: any;
  public culturalPeriod: any;
  public endDateTo: any;
  public endDateFrom: any;
  public startDateFrom: any;
  public identifier: any;
  public startDateTo: any;

  constructor(
      private service: MyService,
      private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      // this.id = params.get('id');
      this.getEventSummary(this.identifier);
      // this.getAllDocById(this.id);
    });
  }

  getEventSummary(identifier: any) {
    this.service.getEventSummary(identifier)
        .subscribe(result => {
          console.log(result);
          // this.identifiers = result.results.bindings;
        });
  }
}
