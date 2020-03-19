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

  ngOnInit() {
    this.getDataNode('string', 'd165dfa1cd274d05a7eea71877f9e0bf');
    this.getSchemaNode('string', 'd165dfa1cd274d05a7eea71877f9e0bf');
  }
  getDataNode(type, uid) {
    this.service.getDataNode(type, uid)
      .subscribe(result => {
        console.log(result);
        this.data = result;
      });
  }

  getSchemaNode(type, uid) {
    this.service.getSchemaNode(type, uid)
      .subscribe(result => {
        console.log(result.definitions.Schema);
        this.schema = result.definitions.Schema;
        this.load = true;
      });
  }


  onSubmit(a: any) {
    this.submittedFormData = a;
    console.log(a);
  }

  showFormSchemaFn($event) {
    console.log($event);
  }

  showFormLayoutFn($event) {
    console.log($event);
  }

  isValid($event) {
    console.log('isvalid ' + $event);
  }

  yourValidationErrorsFn($event) {
    console.log('error' + $event);

  }
  /*schema = {
  type: 'object',
  properties: {
    first_name: { type: 'string' },
    last_name: { type: 'string' },
    email: { type: 'string',
      pattern: '^\\S+@\\S+$',
      description: 'Email will be used for evil.'},
    number: { type: 'number'},
   address: {
      type: 'object',
      properties: {
        street_1: { type: 'string' },
        street_2: { type: 'string' },
        city: { type: 'string' },
        state: {
          type: 'string',
          enum: [ 'AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE',
            'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA',
            'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS',
            'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
            'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD',
            'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY' ]
        },
        zip_code: { type: 'string' }
      }
    },
    notes: { type: 'string' },
    phone_numbers: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          type: { type: 'string', enum: [ 'cell', 'home', 'work' ] },
          number: { type: 'string' }
        },
        required: [ 'type', 'number' ]
      }
    }
  },
  required: [ 'last_name' ]
};
data = {
  first_name: 'Jane', last_name: 25,
  address: {
    street_1: '123 Main St.', street_2: null,
    city: 'Las Vegas', state: 'NV', zip_code: '89123'
  },
  phone_numbers: [
    { number: '702-123-4567', type: 'cell' },
    { number: '702-987-6543', type: 'work' }
  ], notes: ''
};
 */

}
