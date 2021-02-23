import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';
import {MySearchComponent} from '../../../myComponent/mySearchComponent';

@Component({
  selector: 'app-org-search-page',
  templateUrl: './org-search-page.component.html',
  styleUrls: ['./org-search-page.component.css']
})
export class OrgSearchPageComponent extends MySearchComponent implements OnInit {
  public columns: any[] = ['episaIdentifier', 'title', 'dglabIdentifier'];

  constructor(
    private service: MyService,
  ) {
    super({
      name: '',
      identifier: '',
      culturalPeriod: '',
      latitude: '',
      longitude: '',
      keywords: '',
      relatedTo: '',
      location: '',
      buildDateFrom: '',
      buildDateTo: ''
    });
  }

  ngOnInit() {
  }

  getOrgSummary() {
    this.service.getOrgSummary(this.searchObject.identifier)
      .subscribe(result => {
        console.log(result);
        // this.identifiers = result.results.bindings;
      });
  }
}
