import {Component, OnInit} from '@angular/core';
import {MyServiceService} from '../service/my-service.service';
import {ActivatedRoute} from '@angular/router';
import {Location} from '@angular/common';

@Component({
  selector: 'app-edit-entity',
  templateUrl: './edit-entity.component.html',
  styleUrls: ['./edit-entity.component.css']
})
export class EditEntityComponent implements OnInit {

  constructor(
    private location: Location,
    private route: ActivatedRoute,
    private service: MyServiceService) {
  }

  uid = '';
  name = 'Angular 7';
  jsonFormOptions = {
    loadExternalAssets: true,
  };
  schema = {};
  data = {};
  load = false;
  form = {
    schema: {},
    data: {},
    layout: []
  };

  goBack() {
    this.location.back();
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.uid = params.get('uid');
      console.log(this.uid);
      this.load = false;
      // this.getSchemaNode(this.uid);
      this.getSchemaNodeWithTemplate(this.uid);
      console.log('Testing:');
      console.log(this.form);

    });
  }

  getSchemaNodeWithTemplate(uid) {
    this.service.getSchemaNodeWithTemplate(uid)
      .subscribe(returnedSchema => {

        this.form.layout = [];
        console.log('Schema being returned:');
        console.log(returnedSchema);
        this.form.schema = this.refactorSchema(returnedSchema);
        console.log('Refactored Schema');
        console.log(this.form.schema);
        this.form.layout = ['*'];

        this.getDataNodeWithTemplate(this.uid);
        //  this.load = true;
      });
  }

  getDataNodeWithTemplate(uid) {
    this.service.getDataNodeWithTemplate(uid)
      .subscribe(result => {
        this.form.data[this.uid] = result;
        console.log(result);
        console.log('Form Data');
        console.log(this.form.data);
        console.log('ALl Form');
        console.log(this.form);
        this.load = true;
      });
  }

  refactorSchema(jsonSchema) {
    const ref = jsonSchema.$ref;
    const path = ref.split('/');
    const schemaName = path[2];
    const properties = {};
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

  sendNode(data) {
    this.service.sendNode(data)
      .subscribe(result => {
        this.form.data = result;
        console.log('Form Data');
        console.log(this.form.data);
      });
  }

  onSubmit(data: any) {
    console.log(data);

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

  //   getSchemaNode(uid) {
  //   this.service.getSchemaNode(uid)
  //     .subscribe(returnedSchema => {
  //       this.form.layout = [];
  //       console.log(returnedSchema);
  //       this.form.schema = this.refactorSchema(returnedSchema);
  //       this.form.layout = ['*'];
  //       // const button1 = {
  //       //   type: 'submit',
  //       //   title: 'Submit',
  //       //   onClick(evt) {
  //       //     sen
  //       //     evt.preventDefault();
  //       //     alert('Thank you!');
  //       //   }
  //       this.getDataNode(this.uid);
  //       //this.load = true;
  //     });
  // }
  //   getDataNode(uid) {
  //   this.service.getDataNode(uid)
  //     .subscribe(result => {
  //       this.form.data[this.uid] = result;
  //       console.log(result);
  //       this.load = true;
  //     });
  // }
}


// inline ref schema
// const schema3 = {
//           $schema: 'http://json-schema.org/draft-07/schema#',
//           type: 'object',
//           properties: {
//             bb2ca7ccfab44ee49c4594adfde91734: {
//               $ref: '#/definitions/E52_Time_SpanSchema',
//               title: 'Editing E52_Time_Span <a href=\"/bb2ca7ccfab44ee49c4594adfde91734\">teste</a>'
//             }
//           },
//
//           definitions: {
//             DataObjectSchema: {
//               additionalProperties: false,
//               properties: {
//                 name: {
//                   title: 'name',
//                   type: 'string'
//                 },
//                 uid: {
//                   title: 'uid',
//                   type: 'string'
//                 }
//               },
//               required: ['name'],
//               type: 'object'
//             },
//             E52_Time_SpanSchema: {
//               additionalProperties: false,
//               properties: {
//                 date: {
//                   format: 'date',
//                   title: 'date',
//                   type: 'string'
//                 },
//                 has_value: {
//                   items: {
//                     $ref: '#/definitions/DataObjectSchema',
//                     type: 'object'
//                   },
//                   type: 'array'
//                 },
//                 uid: {
//                   title: 'uid',
//                   type: 'string'
//                 },
//                 name: {
//                   title: 'name',
//                   type: 'string'
//                 }
//               },
//               required: ['date', 'name'],
//               type: 'object'
//             }
//           }
//         };

