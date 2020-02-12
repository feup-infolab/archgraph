import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl  } from '@angular/forms';
import {ExampleService} from '../service/example.service';
import {Example} from './example';

@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent {
  register = new FormGroup({
    title: new FormControl(''),
    type: new FormControl('')
  });
  types = ['atribuido', 'formal'];

  constructor(private exampleService: ExampleService) {}
  onSubmit(): void  {
    const dataExample: Example = {type: this.register.value.type, title: this.register.value.title} as Example;
    this.exampleService
      .sendExample(dataExample)
      .subscribe(result => console.log(result));
  }

}
