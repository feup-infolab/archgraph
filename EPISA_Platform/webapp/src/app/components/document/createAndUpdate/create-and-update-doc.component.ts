import {Component, OnInit} from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

import {AlertService, FusekiService} from '../../../service';
import {Title} from '@angular/platform-browser';
import {DocumentComponent} from '../document.component';

@Component({
  selector: 'app-create',
  templateUrl: './create-and-update-doc.component.html',
  styleUrls: ['./create-and-update-doc.component.css', '../../default.css']
})
export class CreateAndUpdateDocComponent extends DocumentComponent {

  public descriptionLevelList: any[] | undefined;


  constructor(protected formBuilder: FormBuilder,
              protected activatedRoute: ActivatedRoute,
              protected router: Router,
              protected service: FusekiService,
              protected titleService: Title,
              protected alertService: AlertService) {
    super(formBuilder, activatedRoute, router, service, titleService, alertService);
    this.getLevelsDescription();
  }

  public loading = false;
  public submitted = false;
  public pageCreateDoc: boolean | undefined;
  public episaIdentifier: any;

  returnUrl: string | undefined;
  error = '';


  getLevelsDescription() {
    this.service.getDescriptionLevels()
      .subscribe(result => {
        this.descriptionLevelList = [];
        result.forEach((item: any) => {
          // @ts-ignore
          this.descriptionLevelList.push(item.descriptionLevel);
        });
      });
  }

  oneElemRequired(arrayName: any) {
    if (!this.getArrayName(arrayName).valid) {
      if (this.getArrayName(arrayName).hasError('required')) {
        this.addElem(arrayName);
        return false;
      }
      return false;
    }
    return true;

  }

  createDoc() {
    this.submitted = true;
    console.log(this.getArrayName('titles').valid);
    if (!this.oneElemRequired('titles')) {
      return;
    }
    if (!this.oneElemRequired('identifiers')) {
      return;
    }
    if (!this.oneElemRequired('descriptionLevel')) {
      return;
    }

    this.loading = true;
    this.service.createDoc(this.docForm.value).subscribe(result => {
        console.log(result);
        this.loading = false;
        if (result.error) {

          this.alertService.error(result.error, this.options);
        } else if (result.message) {

          this.alertService.success(result.message, this.options);
          this.gotoDoc(result.uuid);
        }
      }
    );
  }

  gotoDoc(episaIdentifier: any) {
    this.router.navigate(['doc/' + episaIdentifier]);
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

