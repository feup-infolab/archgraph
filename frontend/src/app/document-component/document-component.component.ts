import {Component, NgModule, OnInit, ViewChild} from '@angular/core';
import {Location} from '@angular/common';
import {ActivatedRoute} from '@angular/router';
import {MyServiceService} from '../service/my-service.service';
import {ComboBoxComponent} from '../combo-box/combo-box.component';
import {NoneComponent} from 'angular7-json-schema-form';
import { MatSliderModule } from '@angular/material/slider';

@Component({
  selector: 'app-document-component',
  templateUrl: './document-component.component.html',
  styleUrls: ['./document-component.component.css']
})
export class DocumentComponentComponent implements OnInit {

  constructor(
    private location: Location,
    private route: ActivatedRoute,
    private service: MyServiceService
  ) { }

  @NgModule ({
   imports: [
   MatSliderModule,
    ]
  })

  panelOpenState = false;

  @ViewChild(ComboBoxComponent) comboBoxReference;
  uid = '';
  name = 'Angular 7';
  schema = {};
  data = {};
  load = false;
  form = {
    schema: {},
    data: {},
    layout: []
  };

  template = {};

  titleType = '';
  titleName = '';
  identifierName = '';
  identifierType = '';



  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.uid = params.get('uid');
      this.load = false;
      // this.getSchemaNode(this.uid);
      this.route.queryParamMap.subscribe(query => {
        this.template = JSON.parse(query.get('template'));
        this.getNodeTemplate(this.uid);
      });
      // this.getNodeTemplate(this.uid);

    });
  }

  getNodeTemplate(uid) {
    this.service.getDocTemplate(uid)
      .subscribe(returnedTemplate => {
        this.template = returnedTemplate;
        console.log(returnedTemplate);
        this.identifierType = returnedTemplate.identifier[0].type;
        this.identifierName = returnedTemplate.identifier[0].value;
        this.titleType = returnedTemplate.title[0].type;
        this.titleName = returnedTemplate.title[0].value;

        console.log(this.identifierType);
        console.log(this.identifierName);
        console.log(this.titleType);
        console.log(this.titleName);
      });
  }

}
