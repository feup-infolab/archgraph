import { Component, OnInit } from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-org-search-page',
  templateUrl: './org-search-page.component.html',
  styleUrls: ['./org-search-page.component.css']
})
export class OrgSearchPageComponent implements OnInit {
  // organization
  public name: any;
  public identifier: any;
  public culturalPeriod: any;
  public latitude: any;
  public longitude: any;
  public keywords: any;
  public relatedTo: any;
  public location: any;
  public buildDateFrom: any;
  public buildDateTo: any;

  constructor(
      private service: MyService,
      private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      // this.id = params.get('id');
      this.getOrgSummary(this.identifier);
      // this.getAllDocById(this.id);
    });
  }

  getOrgSummary(identifier: any) {
    this.service.getOrgSummary(identifier)
        .subscribe(result => {
          console.log(result);
          // this.identifiers = result.results.bindings;
        });
  }
}
