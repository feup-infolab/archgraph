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
  public DescriptionLevel: any;
  public ReferenceCode: any;
  public Keywords: any;
  public RelatedTo: any;
  public ProdDateFrom: any;
  public ProdDateTo: any;
  public InterventionStartDateFrom: any;
  public InterventionStartDateTo: any;
  public InterventionEndDateFrom: any;
  public InterventionEndDateTo: any;
  public CuratorName: any;
  public CreationDateFrom: any;
  public CreationDateTo: any;

  constructor(
      private service: MyService,
      private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      // this.id = params.get('id');
      this.getDocSummary(this.ReferenceCode);
      // this.getAllDocById(this.id);
    });
  }

  getDocSummary(ReferenceCode: any) {
    this.service.getDocSummary(ReferenceCode)
        .subscribe(result => {
          console.log(result);
          // this.identifiers = result.results.bindings;
        });
  }
}
