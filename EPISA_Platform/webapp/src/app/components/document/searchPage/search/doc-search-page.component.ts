import {Component, OnInit} from '@angular/core';
import {FusekiService} from '../../../../service';
import {MySearchComponent} from '../../../myComponent/mySearchComponent';
import {Router} from '@angular/router';

export interface Document {
  episaIdentifier: string;
  title: string;
  dglabIdentifier: string;
}

@Component({
  selector: 'app-doc-search-page',
  templateUrl: './doc-search-page.component.html',
  styleUrls: ['./doc-search-page.component.css', '../../../default.css']
})
export class DocSearchPageComponent extends MySearchComponent implements OnInit {
  public columns: any[] = ['episaIdentifier', 'dglabIdentifier', 'title'];
  public descriptionLevelList: any[] | undefined;

  constructor(
    private router: Router,
    private service: FusekiService,
  ) {
    super({
        title: '',
        descriptionLevel: '',
        prodDateTo: '',
        keywords: '',
        refCode: '',
        prodDateFrom: '',
        relatedTo: '',
        interventionStartDateFrom: '',
        interventionStartDateTo: '',
        interventionEndDateFrom: '',
        interventionEndDateTo: '',
        conservationCuratorName: '',
        digitalCuratorName: '',
        creationDateFrom: '',
        creationDateTo: ''
      }
    );
  }

  ngOnInit() {
    this.getLevelsDescription();
  }

  getResults() {
    this.router.navigate(['/result'], { queryParams: this.searchObject});
  }

  getLevelsDescription() {
    this.service.getDescriptionLevels()
      .subscribe(result => {
        this.descriptionLevelList = [];
        result.forEach((item: any) => {
          // @ts-ignore
          this.descriptionLevelList.push(item.descriptionLevel);
        });
      });
  }
}
