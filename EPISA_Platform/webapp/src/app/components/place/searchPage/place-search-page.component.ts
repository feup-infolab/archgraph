import {Component, OnInit} from '@angular/core';
import {FusekiService} from '../../../service';
import {MySearchComponent} from '../../myComponent/mySearchComponent';

@Component({
  selector: 'app-place-search-page',
  templateUrl: './place-search-page.component.html',
  styleUrls: ['./place-search-page.component.css', '../../default.css']
})
export class PlaceSearchPageComponent extends MySearchComponent implements OnInit {
  public columns: any[] = ['episaIdentifier', 'title', 'dglabIdentifier'];

  constructor(
    private service: FusekiService,
  ) {
    super({
      name: '',
      identifier: '',
      location: '',
      adminDivision: '',
      latitude: '',
      longitude: '',
      keywords: '',
      relatedTo: '',
    });
  }

  ngOnInit() {
  }

  getPlaceSummary() {
    this.service.getPlaceSummary(this.searchObject.identifier)
      .subscribe(result => {
        console.log(result);
      });
  }
}

