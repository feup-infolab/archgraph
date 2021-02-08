import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';
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

  public haveResults: boolean | undefined;
  public dataSource: any;
  public columns: any[] = ['episaIdentifier', 'title', 'dglabIdentifier'];
  public enabledButton: boolean;
  public fieldswithValue: number;

  constructor(
    private service: MyService,
    private route: ActivatedRoute,
  ) {
    this.enabledButton = false;
    this.fieldswithValue = 0;
  }

  ngOnInit() {
  }

  getDocSummary() {

    this.service.getDocSummary(this.referenceCode)
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
      this.fieldswithValue -= 1;
    }
    else {
      this.fieldswithValue += 1;
    }
    if (this.fieldswithValue > 0 ){
      this.enabledButton = true;
    }else {
      this.enabledButton = false;

    }
  }
}
