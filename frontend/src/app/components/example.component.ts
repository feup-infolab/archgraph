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
        const definitions = result.definitions;
        const schema = definitions[Object.keys(definitions)[0]];
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

// inline ref schema
// {
//   "$id": "https://example.com/arrays.schema.json",
//   "$schema": "http://json-schema.org/draft-07/schema#",
//   "description": "A representation of a person, company, organization, or place",
//   "type": "object",
//   "properties": {
//   "fruits": {
//     "type": "array",
//       "items": {
//       "type": "string"
//     }
//   },
//   "vegetables": {
//     "type": "array",
//       "items": { "$ref": "#/definitions/veggie" }
//   }
// },
//   "definitions": {
//   "veggie": {
//     "type": "object",
//       "required": [ "veggieName", "veggieLike" ],
//       "properties": {
//       "veggieName": {
//         "type": "string",
//           "description": "The name of the vegetable."
//       },
//       "veggieLike": {
//         "type": "boolean",
//           "description": "Do I like this vegetable?"
//       }
//     }
//   }
// }
// }

// data
// {
//   "fruits": [ "apple" ],
//   "vegetables": [
//   {
//     "veggieName": "potato",
//     "veggieLike": true
//   },
//   {
//     "veggieName": "broccoli",
//     "veggieLike": false
//   }
// ]
// }



// shema without data____________________________-
// {
//   $schema: 'http://json-schema.org/draft-07/schema#',
//     type: 'object',
//   properties: {
//   vegetables: {
//     $ref: '#/definitions/ola'
//   }
// },
//   definitions: {
//     ola: {
//       type: 'object',
//         required: [ 'veggieName' ],
//         properties: {
//         veggieName: {
//           type: 'string',
//             description: 'The name of the vegetable.'
//         }
//       }
//     }
//   }
// };




