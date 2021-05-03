import {Component, OnInit} from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

import {FusekiService} from '../../../service';
import {Title} from '@angular/platform-browser';
import {DocumentComponent} from '../document.component';

@Component({
  selector: 'app-create',
  templateUrl: './create-and-update-doc.component.html',
  styleUrls: ['./create-and-update-doc.component.css', '../../default.css']
})
export class CreateAndUpdateDocComponent extends DocumentComponent {

  constructor(protected formBuilder: FormBuilder,
              protected activatedRoute: ActivatedRoute,
              protected router: Router,
              protected service: FusekiService,
              protected titleService: Title) {
    super(formBuilder, activatedRoute, router, service, titleService);
  }

  public loading = false;
  public submitted = false;
  public pageCreateDoc: boolean | undefined;
  public episaIdentifier: any;

  returnUrl: string | undefined;
  error = '';




  createDoc() {
    this.submitted = true;
    console.log(this.docForm.controls.titles);

    // stop here if form is invalid
    if (this.docForm.invalid) {
      return;
    }

    this.loading = true;
    this.service.createDoc(this.docForm.value).subscribe(result => {
        console.log(result);
        this.loading = false;
      }
    );
  }

  updateDoc() {
    this.submitted = true;
    console.log(this.docForm.controls.titles);

    // stop here if form is invalid
    if (this.docForm.invalid) {
      return;
    }

    this.loading = true;
    this.service.updateDoc(this.docForm.value, this.episaIdentifier).subscribe(result => {
        console.log(result);
        this.loading = false;
      }
    );
  }
}

