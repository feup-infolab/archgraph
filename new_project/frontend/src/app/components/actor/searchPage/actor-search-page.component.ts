import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';
import {MatTableDataSource} from '@angular/material/table';
import {Document} from "../../document/searchPage/doc-search-page.component";

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

  public haveResults: boolean;
  public dataSource: any;
  public columns: any[] = ['position', 'name', 'weight', 'symbol'];


  constructor(
    private service: MyService,
    private route: ActivatedRoute,
  ) {
    this.haveResults = false;
  }

  ngOnInit() {
  }

  getDocSummary() {
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
}
