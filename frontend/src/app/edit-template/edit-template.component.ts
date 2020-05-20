import {Component, OnInit, ViewChild} from '@angular/core';
import {MyServiceService} from '../service/my-service.service';
import {ActivatedRoute} from '@angular/router';
import {Location} from '@angular/common';
import {ComboBoxComponent} from '../combo-box/combo-box.component';

@Component({
  selector: 'app-edit-template',
  templateUrl: './edit-template.component.html',
  styleUrls: ['./edit-template.component.css']
})
export class EditTemplateComponent implements OnInit {

  constructor(
    private location: Location,
    private route: ActivatedRoute,
    private service: MyServiceService) {
  }


  @ViewChild(ComboBoxComponent) comboBoxReference;
  uid = '';
  name = 'Angular 7';
  jsonFormOptions = {
    loadExternalAssets: true,
  };
  schemaname = '';
  schema = {};
  data = {};
  load = false;
  form = {
    schema: {},
    data: {},
    layout: []
  };
  props = [];
  allprops = {};

  template = {};

  chosenprops = [];

  copyProp;

  goBack() {
    this.location.back();
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.uid = params.get('id');
      console.log('Testing 2:');
      console.log(this.uid);
      this.load = false;
      // this.getSchemaNode(this.uid);
      this.getNodeTemplate(this.uid);
      console.log('Testing:');
      console.log(this.form);

    });
  }

  getNodeTemplate(uid) {
    this.service.getTemplatesFromEntity(uid)
      .subscribe(returnedTemplate => {
        this.getSchemaNodeWithTemplate(uid, returnedTemplate[0]);
    });
  }

  getSchemaNodeWithTemplate(uid, template) {
    this.service.getSchemaNodeWithTemplate(uid, template)
      .subscribe(returnedSchema => {
        this.form.layout = [];
        console.log('The Schema being returned:');
        console.log(returnedSchema[0]);
        this.form.schema = this.refactorSchema(returnedSchema);
        this.form.layout = ['*'];

        this.getDataNodeWithTemplate(this.uid);
        //  this.load = true;
      });
  }

  getDataNodeWithTemplate(uid) {
    this.service.getBaseDataNodeWithTemplate(uid)
      .subscribe(result => {
        this.form.data[this.uid] = result;
        console.log(result);
      });
    this.getAllProperties(this.uid);
  }

  getAllProperties(uid) {
    this.service.geAllSchemaProperties(uid)
      .subscribe(result => {
        console.log('Displaying All Properties:');
        console.log(result);
        console.log(Object.keys(result));
        this.props = Object.keys(result);
        this.allprops = result;
        this.load = true;
      });
    this.getTemplate();
  }

  getTemplate() {
    this.service.getTemplate()
      .subscribe(template => {
        console.log('Displaying Obtained Template:');
        console.log(template);
        this.template = template;
        console.log(this.template);
      });
  }

  refactorSchema(jsonSchema) {
    const ref = jsonSchema.$ref;
    const path = ref.split('/');
    const schemaName = path[2];
    const properties = {};
    this.schemaname = schemaName;
    properties[this.uid] = {
      $ref: ref,
      title: 'Editing'
    };
    jsonSchema.properties = properties;
    jsonSchema.desc = 'Description';

    delete jsonSchema.$ref;
    const schemaEntity = jsonSchema.definitions[schemaName];

    delete schemaEntity.properties.uid;
    jsonSchema.type = 'object';
    return jsonSchema;

  }


  refactorDefinitions(jsonSchema, schema) {
    const ref = jsonSchema.$ref;
    const path = ref.split('/');
    const schemaName = path[2];
    if (schema.definitions[schemaName] !== undefined) {
      console.log('Returned Early');
      return jsonSchema;
    }
    jsonSchema.properties = {name: {title: 'name', type: 'string'}};
    jsonSchema.additionalProperties = false;
    jsonSchema.required = ['name'];
    jsonSchema.type = 'object';
    delete jsonSchema.$ref;
    schema.definitions[schemaName] = jsonSchema;
    return jsonSchema;

  }

  addPropertySchema(property, jsonSchema) {
    jsonSchema.definitions[this.schemaname].properties[property.title] = property;
    this.refactorDefinitions(property.items, this.form.schema);
    return jsonSchema;
  }

  sendNode(data) {
    this.service.sendNode(data, data)
      .subscribe(result => {
        this.form.data = result;
        console.log(result);
      });
  }

  addProp() {
    this.load = false;
    this.chosenprops.push(this.comboBoxReference.inputItem);
    this.form.data[this.uid][this.comboBoxReference.inputItem] = [];
    this.form.data[this.uid][this.comboBoxReference.inputItem][0] = {name: '1', uid: '1' };
    const schemaEntity = this.schemaname.replace('Schema', '');
    this.template[schemaEntity][this.comboBoxReference.inputItem] = this.allprops[this.comboBoxReference.inputItem].items.$ref
      .replace('Schema', '').replace('#/definitions/', '');
    this.form.schema = this.addPropertySchema(this.allprops[this.comboBoxReference.inputItem], this.form.schema);
    this.sendProps();
  }


  sendProps() {
    this.service.sendTemplate(this.template)
      .subscribe( result => {
        this.load = true;
      });
  }

  onSubmit(data: any) {

    this.sendNode(data);
  }

  showFormSchemaFn($event) {
    // console.log($event); it shows schema of node
  }

  showFormLayoutFn($event) {
    console.log($event);
  }

  isValid($event) {
    // console.log('isvalid ' + $event);
  }

  yourValidationErrorsFn($event) {
    console.log('error' + $event);

  }
}
