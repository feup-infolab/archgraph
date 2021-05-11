import {Component, OnInit} from '@angular/core';
import {FusekiService} from '../../../service/fuseki.service';
import {MatTableDataSource} from '@angular/material/table';
import {MySearchComponent} from '../../myComponent/mySearchComponent';

export interface Document {
  episaIdentifier: string;
  title: string;
  dglabIdentifier: string;
}

// export interface DocSearchObject {
//   title: any;
//   descriptionLevel: any;
//   prodDateTo: any;
//   keywords: any;
//   refCode: any;
//   prodDateFrom: any;
//   relatedTo: any;
//   interventionStartDateFrom: any;
//   interventionStartDateTo: any;
//   interventionEndDateFrom: any;
//   interventionEndDateTo: any;
//   curatorName: any;
//   creationDateFrom: any;
//   creationDateTo: any;
// }


@Component({
  selector: 'app-doc-search-page',
  templateUrl: './doc-search-page.component.html',
  styleUrls: ['./doc-search-page.component.css', '../../default.css']
})
export class DocSearchPageComponent extends MySearchComponent implements OnInit {
  public columns: any[] = ['episaIdentifier', 'dglabIdentifier', 'title'];
  public descriptionLevelList: any[] | undefined;

  constructor(
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

  getDocSummary() {
    this.service.getDocSummary(this.searchObject)
      .subscribe(result => {
        console.log(result);
        const elements = [];
        for (const elem of result) {
          const element = {
            episaIdentifier: elem.episaIdentifier,
            title: elem.title,
            dglabIdentifier: elem.dglabIdentifier
          };
          elements.push(element);
        }
        this.dataSource = new MatTableDataSource<Document>(elements);
        if (this.dataSource.data.length > 0) {
          this.haveResults = true;
        }
      });

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
