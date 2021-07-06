import {Component, OnInit} from '@angular/core';
import {Location} from '@angular/common';
import {Router} from '@angular/router';
import {ActivatedRoute} from '@angular/router';
import {FusekiService} from '../../../../service';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css', '../../../default.css']
})
export class ResultComponent implements OnInit {
  public records: any[] | undefined;
  public searchObject: any;
  public hasResult: boolean | undefined;


  constructor(private location: Location,
              private router: ActivatedRoute,
              private service: FusekiService) {
    this.router.queryParamMap.subscribe((params) => {
        this.searchObject = {...params.keys, ...params};
      }
    );
  }

  ngOnInit(): void {
    this.getDocSummary();
  }

  goBack() {
    this.location.back();
  }

  getDocSummary() {
    this.service.getDocSummary(this.searchObject.params)
      .subscribe(result => {
        console.log(result);
        const elements = [];
        this.records = [];
        for (const elem of result) {
          const element = {
            episaIdentifier: elem.episaIdentifier,
            titles: elem.titles,
            dglabIdentifier: elem.dglabIdentifier,
            physicalLocation: elem.physicalLocation
          };
          elements.push(element);
          this.records.push(element);
          if (this.records.length === 0) {
            this.hasResult = false;
          } else {
            this.hasResult = true;
          }

        }
      });

  }
}
