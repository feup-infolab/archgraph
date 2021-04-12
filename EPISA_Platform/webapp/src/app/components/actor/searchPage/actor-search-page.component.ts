import {Component, OnInit} from '@angular/core';
import {FusekiService} from '../../../service/fuseki.service';
import {MatTableDataSource} from '@angular/material/table';
import {MySearchComponent} from '../../myComponent/mySearchComponent';

export interface Actor {
  episaIdentifier: string;
  title: string;
  dglabIdentifier: string;
}

// export interface ActorSearchObject {
//   name: any;
//   birthDateTo: any;
//   birthDateFrom: any;
//   deathDateFrom: any;
//   deathDateTo: any;
//   keywords: any;
//   relatedTo: any;
//   identifier: any;
//   culturalPeriod: any;
//   episaIdentifier: any;
// }


@Component({
  selector: 'app-actor-search-page',
  templateUrl: './actor-search-page.component.html',
  styleUrls: ['./actor-search-page.component.css', '../../default.css']
})
export class ActorSearchPageComponent extends MySearchComponent implements OnInit {
  public columns: any[] = ['episaIdentifier', 'dglabIdentifier', 'title'];

  constructor(
    private service: FusekiService,
  ) {
    super({
      name: '',
      birthDateTo: '',
      birthDateFrom: '',
      deathDateFrom: '',
      deathDateTo: '',
      keywords: '',
      relatedTo: '',
      identifier: '',
      culturalPeriod: '',
      episaIdentifier: '',
    });
  }

  ngOnInit() {
  }

  getActorSummary() {
    this.service.getActorSummary(this.searchObject.identifier)
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
}
