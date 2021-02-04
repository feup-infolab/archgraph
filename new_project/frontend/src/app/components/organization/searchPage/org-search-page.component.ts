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
  public Name: any;
  public Identifier: any;
  public CulturalPeriod: any;
  public Latitude: any;
  public Longitude: any;
  public Keywords: any;
  public RelatedTo: any;
  public Location: any;
  public BuildDateFrom: any;
  public BuildDateTo: any;

  constructor(
      private service: MyService,
      private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      // this.id = params.get('id');
      this.getOrgSummary(this.Identifier);
      // this.getAllDocById(this.id);
    });
  }

  getOrgSummary(Identifier: any) {
    this.service.getOrgSummary(Identifier)
        .subscribe(result => {
          console.log(result);
          // this.identifiers = result.results.bindings;
        });
  }
}
