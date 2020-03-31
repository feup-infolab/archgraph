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
  searched = '';
  searchResult = {};
  searchResultString = '';
  uid = '';
  name = 'Angular 7';
  jsonFormOptions = {
    loadExternalAssets: true,
  };
  schema = {};
  data = {};
  submittedFormData;
  load = false;
  loadSearch = false;
  form = {
      schema: {
    },
    data : {
      },
    layout: [

    ]
  };
  onEnter(uid: string) {
    this.uid = uid;
    // this.form.data = {};
    // this.form.layout = [];
    // this.form.schema = {};
    this.load = false;
    this.getSchemaNode(this.uid);
  }
  searchDatabase(searched: string) {
    this.searched = searched;
    this.loadSearch = false;
    this.getSearchJson(this.searched);
  }

  getSearchJson(search) {
    this.service.getSearchJson( search)
      .subscribe(result => {
        this.searchResult = result;
        this.searchResultString = JSON.stringify(result);
        console.log(result);
        this.loadSearch = true;
      });
  }

ngOnInit() {

  }
 getDataNode(uid) {
    this.service.getDataNode( uid)
      .subscribe(result => {
        this.form.data = result;
        console.log(result);
        this.load = true;
      });
  }

getSchemaNode(uid) {
    this.service.getSchemaNode(uid)
      .subscribe(result => {
        this.form.layout = [];
        console.log(result);

        const schema = result.definitions.Schema;
        this.form.schema = schema;
        const cloneProperties = {...schema.properties};
        delete cloneProperties.uid;
        Object.keys(cloneProperties).forEach((n, i) => {
          const object = { key: n};
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
        this.getDataNode(this.uid);

      });
  }



sendNode(data) {
    this.service.sendNode( data)
      .subscribe(result => {
        this.form.data = result;
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

// {
//   "schema": {
//   "properties": {
//     "animal": {
//       "$ref": "#/definitions/animation"
//     }
//   },
//   "definitions": {
//     "animation": {
//       "type": "object",
//         "properties": {
//         "duration": {
//           "title": "Duration",
//             "type": "integer"
//         },
//         "stepper": {
//           "title": "Stepper",
//             "type": "string"
//         },
//         "then": {
//           "title": "Then",
//             "type": "array",
//             "maxItems": 1,
//             "items": {
//             "$ref": "#/definitions/animation"
//           },
//           "default": []
//         }
//       }
//     }
//   }
// }
// }
