import {Component, OnInit} from '@angular/core';
import {FusekiService} from '../../../service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-restoration',
  templateUrl: './restoration.component.html',
  styleUrls: ['./restoration.component.css', '../../default.css']
})
export class RestorationComponent implements OnInit {
  public titles: any[];
  public id: any;


  constructor(
    private service: FusekiService,
    private route: ActivatedRoute,
  ) {
    this.titles = [];
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
      // this.getNotes(this.id);
      // this.getSuppliedTitle(this.id);
    });
  }

}
