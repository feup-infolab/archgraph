import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {MatTableDataSource} from '@angular/material/table';

export interface Document {
  episaIdentifier: string;
  title: string;
  dglabIdentifier: string;
}


@Component({
  selector: 'app-doc-search-page',
  templateUrl: './doc-search-page.component.html',
  styleUrls: ['./doc-search-page.component.css']
})
export class DocSearchPageComponent implements OnInit {
  public haveResults: boolean | undefined;
  public dataSource: any;
  public columns: any[] = ['episaIdentifier', 'title', 'dglabIdentifier'];
  public enabledButton: boolean;
  public fieldsWithValue: number;
  public descriptionLevelList: any[] = ['option1', 'option2', 'option3'];
  public formOldValue: any;
  public searchObject: {
    title: any
    descriptionLevel: any;
    prodDateTo: any;
    keywords: any;
    refCode: any;
    prodDateFrom: any;
    relatedTo: any;
    interventionStartDateFrom: any;
    interventionStartDateTo: any;
    interventionEndDateFrom: any;
    interventionEndDateTo: any;
    curatorName: any;
    creationDateFrom: any;
    creationDateTo: any;
  };


  constructor(
    private service: MyService,
  ) {
    this.enabledButton = false;
    this.fieldsWithValue = 0;
    this.searchObject = {
      title: '',
      descriptionLevel: '',
      prodDateTo: '',
      keywords: '',
      prodDateFrom: '',
      relatedTo: '',
      interventionStartDateFrom: '',
      interventionStartDateTo: '',
      interventionEndDateFrom: '',
      interventionEndDateTo: '',
      curatorName: '',
      creationDateFrom: '',
      creationDateTo: '',
      refCode: '',
    };
  }

  ngOnInit() {
  }

  getDocSummary() {
    this.service.getDocSummary(this.searchObject)
      .subscribe(result => {
        console.log(result);
        const elements = [];
        // tslint:disable-next-line:prefer-for-of
        for (let i = 0; i < result.length; i++) {
          const element = {
            episaIdentifier: result[i].episaIdentifier,
            title: result[i].title,
            dglabIdentifier: result[i].dglabIdentifier
          };
          elements.push(element);
        }
        this.dataSource = new MatTableDataSource<Document>(elements);
        if (this.dataSource.data.length > 0) {
          this.haveResults = true;
        }
      });

  }

  setHaveResults() {
    this.haveResults = false;
  }

  dataChanged(newObj: any) {
    if (this.formOldValue === '' || this.formOldValue === undefined) {
      if (newObj !== '' || newObj !== undefined) {
        this.fieldsWithValue += 1;
      }
    }
    if (this.formOldValue !== '' || this.formOldValue !== undefined) {
      if (newObj === '' || newObj === undefined) {
        this.fieldsWithValue -= 1;
      }
    }
    //   if (optional) {
    //     if (this.searchObject.descriptionLevel === undefined && newObj !== undefined) {
    //       this.fieldsWithValue += 1;
    //     } else if (this.searchObject.descriptionLevel !== undefined && newObj === undefined) {
    //       this.fieldsWithValue -= 1;
    //     }
    //   } else if (newObj === '') {
    //     this.fieldsWithValue -= 1;
    //   } else {
    //     this.fieldsWithValue += 1;
    //   }
    console.log(this.fieldsWithValue);
    this.enabledButton = this.fieldsWithValue > 0;
  }
}
