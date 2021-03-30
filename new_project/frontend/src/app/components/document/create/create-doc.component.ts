import {Component, OnInit} from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {first} from 'rxjs/operators';
import {FormArray} from '@angular/forms';


import {MyService} from '../../../service';

@Component({
  selector: 'app-create',
  templateUrl: './create-doc.component.html',
  styleUrls: ['./create-doc.component.css']
})
export class CreateDocComponent implements OnInit {
  public docForm: FormGroup;
  public loading = false;
  public submitted = false;
  returnUrl: string | undefined;
  error = '';

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private service: MyService,
  ) {
    this.docForm = this.formBuilder.group({
      title: ['', Validators.required],
      type: ['', Validators.required],
      materials: this.formBuilder.group({
        material: [''],
        component: ['']
      }),
      dimensions: this.formBuilder.group({
        dimension: [''],
        value: [''],
        measurementUnit: [''],
        component: ['']
      })
    });
    // if (this.service.getObservableUser()) {
    //   this.router.navigate(['/']);
    // }
  }

  ngOnInit() {
    // get return url from route parameters or default to '/'
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/';
  }

  get formControls() {
    return this.docForm.controls;
  }

  createDoc() {
    this.submitted = true;
    console.log(this.docForm.controls.title.errors);

    // stop here if form is invalid
    if (this.docForm.invalid) {
      return;
    }

    this.loading = true;
    this.service.createDoc(this.docForm.value)
      .subscribe(result => {
          console.log(result);
        }
      );
  }

  goToHome() {
    this.router.navigate(['/']);
  }
}

