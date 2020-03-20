import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl  } from '@angular/forms';
import {Schema} from './Schema';
import {MyServiceService} from '../service/my-service.service';

@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent implements OnInit {

  constructor(private service: MyServiceService) {  }
  name = 'Angular 7';
  jsonFormOptions = {
    loadExternalAssets: true,
  };
  schema = {};
  data = {};
  submittedFormData;
  load = false;
  form = {
      schema: {
    },
    data : {
      },
    layout: [

    ]
  };

ngOnInit() {
    this.getDataNode('f40582c49afd43d7b8ac1b394d030b1c');
    this.getSchemaNode('f40582c49afd43d7b8ac1b394d030b1c');
  }
getDataNode(uid) {
    this.service.getDataNode( uid)
      .subscribe(result => {
        this.form.data = result;
        console.log(result);
      });
  }

getSchemaNode(uid) {
    this.service.getSchemaNode(uid)
      .subscribe(result => {
        const schema = result.definitions.Schema;
        this.form.schema = schema;
        const cloneProperties = {...schema.properties};

        delete cloneProperties.uid;

        Object.keys(cloneProperties).forEach((n, i) => {
          const type = cloneProperties[n].type;
          const object = { key: n, dataType: type};
          this.form.layout.push(object);
        });
        // const button1 = {
        //   type: 'submit',
        //   title: 'Submit',
        //   onClick(evt) {
        //     sen
        //     evt.preventDefault();
        //     alert('Thank you!');
        //   }

        console.log(this.form.layout);
        this.load = true;
      });
  }



sendNode(data) {
    this.service.sendNode( data)
      .subscribe(result => {
        console.log(result);
      });
  }


onSubmit(a: any) {
    this.sendNode(a);
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
