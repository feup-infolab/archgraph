import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {MatTableDataSource} from '@angular/material/table';

export interface Actor {
  episaIdentifier: string;
  title: string;
  dglabIdentifier: string;
}

@Component({
  selector: 'app-actor-search-page',
  templateUrl: './actor-search-page.component.html',
  styleUrls: ['./actor-search-page.component.css']
})
export class ActorSearchPageComponent implements OnInit {
  public name: any;
  public birthDateTo: any;
  public birthDateFrom: any;
  public deathDateFrom: any;
  public deathDateTo: any;
  public keywords: any;
  public relatedTo: any;
  public identifier: any;
  public culturalPeriod: any;
  public episaIdentifier: any;

  public haveResults: boolean | undefined;
  public dataSource: any;
  public columns: any[] = ['episaIdentifier', 'title', 'dglabIdentifier'];
  public enabledButton: boolean;
  public fieldswithValue: number;


  constructor(
    private service: MyService,
  ) {
    this.haveResults = false;
    this.enabledButton = false;
    this.fieldswithValue = 0;
  }

  ngOnInit() {
  }

  getActorSummary() {
    this.service.getActorSummary(this.identifier)
      .subscribe(result => {
        console.log(result);
        const elements = [];
        const element = {
          episaIdentifier: result.episaIdentifier,
          title: result.title,
          dglabIdentifier: result.dglabIdentifier
        };
        elements.push(element);
        this.dataSource = new MatTableDataSource<Actor>(elements);
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
    } else {
      this.fieldswithValue += 1;
    }
    this.enabledButton = this.fieldswithValue > 0;
  }
}
