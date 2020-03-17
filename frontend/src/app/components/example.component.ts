import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl  } from '@angular/forms';
import {Example} from './example';
import {MyServiceService} from '../service/my-service.service';

@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent implements OnInit {

  constructor(private service: MyServiceService) {  }
  records: {};
  name = 'Angular 6';
  jsonFormOptions = {
    loadExternalAssets: false,
  };
  schema = {
    type: 'object',
    properties: {
      first_name: { type: 'string' },
      last_name: { type: 'string' },
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
      birthday: { type: 'string' },
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
  submittedFormData;

  ngOnInit() {
    console.log('ola');
    this.service.getExample()
      .subscribe(result => {
        this.records = result;
        console.log(result);
      });
  }


  onSubmit(data: any) {
    this.submittedFormData = data;
  }

  showFormSchemaFn($event) {
    console.log($event);
  }

  showFormLayoutFn($event) {
    console.log($event);
  }
}
