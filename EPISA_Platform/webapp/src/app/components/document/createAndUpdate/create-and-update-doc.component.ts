import {Component, OnInit} from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Location} from '@angular/common';

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
              protected alertService: AlertService,
              protected location: Location) {
    super(formBuilder, activatedRoute, router, service, titleService, alertService, location);
    this.getLevelsDescription();
    this.addElem('descriptionLevel');
    this.addElem('titles');
    this.addElem('identifiers');
  }

  public loading = false;
  public submitted = false;
  public pageCreateDoc: boolean | undefined;
  public episaIdentifier: any;

  returnUrl: string | undefined;
  error = '';
  changed = false;


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

  createDoc() {

    // this.loading = true;
    this.service.createDoc(this.docForm.value).subscribe(result => {
        console.log(result);
        // this.loading = false;
        if (result.message) {
          this.alertService.success(result.message, this.options);
          this.gotoDoc(result.uuid);
        }
      }
    );
  }

  gotoDoc(episaIdentifier: any) {
    this.router.navigate(['doc/' + episaIdentifier]);
  }

  invalidForm() {
    // stop here if form is invalid
    return this.docForm.invalid ||
      this.getArrayName('titles').invalid ||
      !this.OneActivesElems('titles') ||
      this.getArrayName('identifiers').invalid ||
      !this.OneActivesElems('identifiers') ||
      this.getArrayName('descriptionLevel').invalid ||
      !this.OneActivesElems('descriptionLevel');
  }

  resetStatusFromArray(arrayName: any) {
    const myArray = this.getArrayName(arrayName);
    for (let i = 0; i < myArray.length; i++) {
      const newValue = Object.assign(myArray.at(i).value, {status: 'notChanged'});
      myArray.at(i).setValue(newValue);
    }
  }

  updateDoc() {
    this.submitted = true;

    if (this.invalidForm()) {
      return;
    }

    this.loading = true;
    this.service.updateDoc(this.docForm.getRawValue(), this.episaIdentifier).subscribe(result => {
      console.log(result);
      this.loading = false;
      if (result.message) {
        this.alertService.success(result.message, this.options);
        this.resetStatusFromAllArrays();
      }
    });
  }

  resetStatusFromAllArrays() {
    this.resetStatusFromArray('titles');
    this.resetStatusFromArray('identifiers');
    this.resetStatusFromArray('accessConditions');
    this.resetStatusFromArray('descriptionLevel');
    this.resetStatusFromArray('dimensions');
    this.resetStatusFromArray('quantities');
    this.resetStatusFromArray('typologies');
    this.resetStatusFromArray('materials');
    this.resetStatusFromArray('documentaryTraditions');
    this.resetStatusFromArray('subjects');
    this.resetStatusFromArray('relatedDocs');
    this.resetStatusFromArray('languages');
    this.resetStatusFromArray('writings');
  }

  deleteDoc() {
    this.submitted = true;
    console.log(this.docForm.controls.titles);

    // stop here if form is invalid
    if (this.docForm.invalid) {
      return;
    }

    this.loading = true;
    this.service.deleteDoc(this.episaIdentifier).subscribe(result => {
        console.log(result);
        this.loading = false;
        if (result.error) {

          this.alertService.error(result.error, this.options);
        } else if (result.message) {
          this.alertService.success(result.message, this.options);
          this.goToHome();
        }
      }
    );
  }
}


