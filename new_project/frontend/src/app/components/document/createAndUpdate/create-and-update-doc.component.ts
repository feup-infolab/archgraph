import {Component, OnInit} from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {FormArray} from '@angular/forms';


import {FusekiService} from '../../../service';
import {Title} from '@angular/platform-browser';

@Component({
  selector: 'app-create',
  templateUrl: './create-and-update-doc.component.html',
  styleUrls: ['./create-and-update-doc.component.css', '../../default.css']
})
export class CreateAndUpdateDocComponent implements OnInit {
  public docForm: FormGroup;
  public loading = false;
  public submitted = false;
  public pageCreateDoc: boolean | undefined;
  returnUrl: string | undefined;
  error = '';
  title = 'FormArray Example in Angular Reactive forms';

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private service: FusekiService,
    private titleService: Title
  ) {


    this.docForm = this.formBuilder.group({
      titles: this.formBuilder.array([]),
      identifiers: this.formBuilder.array([]),
      materials: this.formBuilder.array([]),
      dimensions: this.formBuilder.array([]),
      quantities: this.formBuilder.array([]),
      conservationStates: this.formBuilder.array([]),
      languages: this.formBuilder.array([]),
      writings: this.formBuilder.array([]),
      documentaryTraditions: this.formBuilder.array([]),
      typologies: this.formBuilder.array([]),
      subjects: this.formBuilder.array([]),
      accessConditions: this.formBuilder.array([]),
      relatedDocs: this.formBuilder.array([]),
    });
    // if (this.service.getObservableUser()) {
    //   this.router.navigate(['/']);
    // }
  }

  ngOnInit() {
    const href = this.router.url;
    console.log(this.router.url);
    // tslint:disable-next-line:variable-name
    this.pageCreateDoc = href.includes('create');
    if (!this.pageCreateDoc) {
      this.route.paramMap.subscribe(params => {
        const episaIdentifier = params.get('id') || 'id';
        this.getDocById(episaIdentifier);
        this.setDocTitle(episaIdentifier);
      });
    }

    console.log(this.pageCreateDoc);
    // get return url from route parameters or default to '/'
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/';
  }

  setDocTitle(title: string) {
    this.titleService.setTitle('Doc ' + title);
  }

  // ========== new Elems ==================
  newTitle(): FormGroup {
    return this.formBuilder.group({
      title: '',
      type: '',
    });
  }

  newIdentifier(): FormGroup {
    return this.formBuilder.group({
      identifier: '',
      type: '',
    });
  }

  newMaterial(): FormGroup {
    return this.formBuilder.group({
      material: '',
      component: '',
    });
  }

  newDimensionQuantity(): FormGroup {
    return this.formBuilder.group({
      dimension: '',
      value: '',
      measurementUnit: '',
      component: ''
    });
  }

  newConservationStatus(): FormGroup {
    return this.formBuilder.group({
      conservationStatus: '',
      initialDate: '',
      finalDate: '',
    });
  }

  newLanguage(): FormGroup {
    return this.formBuilder.group({
      language: '',
      identifier: '',
    });
  }

  newWriting(): FormGroup {
    return this.formBuilder.group({
      writing: '',
      identifier: '',
    });
  }

  newDocumentaryTradition(): FormGroup {
    return this.formBuilder.group({
      documentaryTradition: '',
    });
  }

  newTypology(): FormGroup {
    return this.formBuilder.group({
      documentaryTypology: '',
    });
  }

  newSubject(): FormGroup {
    return this.formBuilder.group({
      subject: '',
    });
  }

  newAccessCondition(): FormGroup {
    return this.formBuilder.group({
      accessCondition: '',
      justification: '',

    });
  }

  newRelatedDoc(): FormGroup {
    return this.formBuilder.group({
      recordIdentifier: '',
      title: '',
      relationType: '',
    });
  }

// =========End New Elems ===================

  getArrayName(arrayName: string): FormArray {
    return this.docForm.get(arrayName) as FormArray;
  }


  setArrayValue(arrayName: string, arrayValue: any) {
    const myArray = this.getArrayName(arrayName);

    while (myArray.value.length < arrayValue.length) {
      this.addElem(arrayName);

    }
    myArray.setValue(arrayValue);
  }


  addElem(arrayName: string) {
    let newElem;
    switch (arrayName) {
      case'materials':
        newElem = this.newMaterial();
        break;
      case'dimensions':
        newElem = this.newDimensionQuantity();
        break;
      case'identifiers':
        newElem = this.newIdentifier();
        break;
      case'titles':
        newElem = this.newTitle();
        break;
      case'quantities':
        newElem = this.newDimensionQuantity();
        break;
      case'conservationStates':
        newElem = this.newConservationStatus();
        break;
      case'languages':
        newElem = this.newLanguage();
        break;
      case'writings':
        newElem = this.newWriting();
        break;
      case'documentaryTraditions':
        newElem = this.newDocumentaryTradition();
        break;
      case'typologies':
        newElem = this.newTypology();
        break;
      case'subjects':
        newElem = this.newSubject();
        break;
      case'accessConditions':
        newElem = this.newAccessCondition();
        break;
      case'relatedDocs':
        newElem = this.newRelatedDoc();
        break;


    }
    // @ts-ignore
    this.getArrayName(arrayName).push(newElem);
  }

  removeElem(arrayName: string, i: number) {
    const myArray = this.getArrayName(arrayName);
    myArray.removeAt(i);
  }

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
    this.service.updateDoc(this.docForm.value).subscribe(result => {
        console.log(result);
      }
    );
  }


  goToHome() {
    this.router.navigate(['/']);
  }


  getDocById(id: any) {
    this.service.getDocById(id)
      .subscribe(result => {
          console.log(result);
          this.setArrayValue('titles', result.titles);
          this.setArrayValue('identifiers', result.identifiers);
          this.setArrayValue('accessConditions', result.accessConditions);
          this.setArrayValue('dimensions', result.dimensions);
          this.setArrayValue('quantities', result.quantities);
          this.setArrayValue('typologies', result.typologies);
          this.setArrayValue('materials', result.materials);
          this.setArrayValue('documentaryTraditions', result.documentaryTraditions);
          this.setArrayValue('subjects', result.subjects);
          this.setArrayValue('relatedDocs', result.relatedDocs);
          this.setArrayValue('languages', result.languages);
          this.setArrayValue('writings', result.writings);
          this.setArrayValue('conservationStates', result.conservationStates);


          /*
                    const elements = [];
                    for (const relatedoc of result.relatedDocuments) {
                      const element = {
                        episaIdentifier: relatedoc.episaIdentifier,
                        title: relatedoc.title,
                        dglabIdentifier: relatedoc.dglabIdentifier
                      };
                      elements.push(element);
                    }
                    this.dataSource = new MatTableDataSource<Document>(elements);
                    if (this.dataSource.data.length > 0) {
                      this.haveResults = true;
                    }*/
        }
      );
  }
}

