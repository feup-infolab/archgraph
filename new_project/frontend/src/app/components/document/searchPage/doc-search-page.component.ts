import { Component, OnInit } from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-doc-search-page',
  templateUrl: './doc-search-page.component.html',
  styleUrls: ['./doc-search-page.component.css']
})
export class DocSearchPageComponent implements OnInit {
  // document
  public descriptionLevel: any;
  public referenceCode: any;
  public keywords: any;
  public relatedTo: any;
  public prodDateFrom: any;
  public prodDateTo: any;
  public interventionStartDateFrom: any;
  public interventionStartDateTo: any;
  public interventionEndDateFrom: any;
  public interventionEndDateTo: any;
  public curatorName: any;
  public creationDateFrom: any;
  public creationDateTo: any;

  constructor(
      private service: MyService,
      private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      // this.id = params.get('id');
      this.getDocSummary(this.referenceCode);
      // this.getAllDocById(this.id);
    });
  }

  getDocSummary(referenceCode: any) {
    this.service.getDocSummary(referenceCode)
        .subscribe(result => {
          console.log(result);
          // this.identifiers = result.results.bindings;
        });
  }
}
