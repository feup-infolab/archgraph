import {Component, OnInit} from '@angular/core';
import {FusekiService} from '../../service/fuseki.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-organization',
  templateUrl: './organization.component.html',
  styleUrls: ['./organization.component.css', '../default.css']
})
export class OrganizationComponent implements OnInit {

  private id: any;

  constructor(
    private service: FusekiService,
    private route: ActivatedRoute,
  ) {
    // this.titles = [];
    // this.notes = [];
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
      // this.getNotes(this.id);
      // this.getSuppliedTitle(this.id);
    });
  }

}
