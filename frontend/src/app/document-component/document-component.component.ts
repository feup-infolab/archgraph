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

  ftitleType = '';
  ftitleName = '';
  fidentifierName = '';
  fidentifierType = '';
  titleType = '';
  titleName = '';
  identifierName = '';
  identifierType = '';
  titleTypeVal = '';
  identifierTypeVal = '';

  titleTypes = [];
  identifierTypes = [];

  id = {
    value: '',
    type: ''
  };

  titlef = {
    value: '',
    type: ''
  };

  deliveredJson = {
    identifier : [],
    title: []
  };



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
        this.identifierType = returnedTemplate.identifier[0].type;
        this.identifierName = returnedTemplate.identifier[0].value;
        this.titleType = returnedTemplate.title[0].type;
        this.titleName = returnedTemplate.title[0].value;
        this.fidentifierType = returnedTemplate.identifier[0].type;
        this.fidentifierName = returnedTemplate.identifier[0].value;
        this.ftitleType = returnedTemplate.title[0].type;
        this.ftitleName = returnedTemplate.title[0].value;
        this.getTitleTypes();
      });
  }

  getTitleTypes() {
    this.service.getAllTitleTypes()
      .subscribe(returnedTitles => {
        this.titleTypes = returnedTitles;
        this.getIdentifierTypes();
      });

  }

  getIdentifierTypes() {
    this.service.getAllIdentifierTypes()
      .subscribe(returnedIdentifiers => {
        this.identifierTypes = returnedIdentifiers;
        console.log(returnedIdentifiers);
      });

  }

  submitUpdate() {

    let j: any;
    // tslint:disable-next-line:forin
    for (j in this.titleTypes) {
      if (j.option === this.titleType) {
        this.titleTypeVal = j.value;
      }
    }
    // tslint:disable-next-line:forin
    for (j in this.identifierTypes) {
      if (j.option === this.identifierType) {
        this.identifierTypeVal = j.value;
      }
    }
    this.deliveredJson.identifier.push({value: this.identifierName, type: this.identifierTypeVal});
    this.deliveredJson.title.push({value: this.titleName, type: this.titleTypeVal});
  }

  checkChange() {

    // tslint:disable-next-line:max-line-length
    return this.ftitleName === this.titleName && this.fidentifierName === this.identifierName && this.fidentifierType === this.identifierType && this.ftitleType === this.titleType;

  }

}
