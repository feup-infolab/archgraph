import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {MySearchComponent} from '../../../myComponent/mySearchComponent';

@Component({
  selector: 'app-place-search-page',
  templateUrl: './place-search-page.component.html',
  styleUrls: ['./place-search-page.component.css']
})
export class PlaceSearchPageComponent extends MySearchComponent implements OnInit {
  public columns: any[] = ['episaIdentifier', 'title', 'dglabIdentifier'];

  constructor(
    private service: MyService,
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

