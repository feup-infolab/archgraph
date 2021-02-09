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
        const element = {
          episaIdentifier: result.episaIdentifier,
          title: result.title,
          dglabIdentifier: result.dglabIdentifier
        };
        elements.push(element);
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
    console.log(newObj);
    if (newObj === '') {
      this.fieldsWithValue -= 1;
    } else {
      this.fieldsWithValue += 1;
    }
    this.enabledButton = this.fieldsWithValue > 0;
  }
}
