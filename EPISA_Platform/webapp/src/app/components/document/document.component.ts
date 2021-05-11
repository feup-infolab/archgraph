import {Component, OnInit} from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {FormArray} from '@angular/forms';


import {AlertService, FusekiService, UserService} from '../../service';
import {Title} from '@angular/platform-browser';
import {MatTableDataSource} from '@angular/material/table';
import {Document} from './searchPage/doc-search-page.component';

@Component({
  selector: 'app-my',
  templateUrl: './document.component.html',
  styleUrls: ['./document.component.css', '../default.css']
})
export class DocumentComponent implements OnInit {

  public docForm: FormGroup;
  public loading = false;
  public submitted = false;
  public pageCreateDoc: boolean | undefined;
  public episaIdentifier: any;
  public haveResults: boolean | undefined;
  public dataSource: any;
  public columns: any[] = ['episaIdentifier', 'dglabIdentifier', 'title'];
  public isExpanded: boolean | undefined;
  public myTitleTypes: any = [{value: 'formalTitle', viewValue: 'Formal Title'}, {value: 'suppliedTitle', viewValue: 'Supplied Title'}];
  public myIdentifierTypes: any = [{value: 'referenceCode', viewValue: 'Reference Code'}];
  protected options = {
    autoClose: true,
    keepAfterRouteChange: false
  };


  constructor(
    protected formBuilder: FormBuilder,
    protected activatedRoute: ActivatedRoute,
    protected router: Router,
    protected service: FusekiService,
    protected titleService: Title,
    protected alertService: AlertService
  ) {

    this.docForm = this.formBuilder.group({
      DOC_IDENTITY: this.formBuilder.group({
        titles: this.formBuilder.array([], Validators.compose([Validators.required, Validators.minLength(1)])),
        // descriptionLevel: formBuilder.control(''),
        identifiers: this.formBuilder.array([], Validators.compose([Validators.required, Validators.minLength(1)])),
        materials: this.formBuilder.array([]),
        dimensions: this.formBuilder.array([]),
        quantities: this.formBuilder.array([]),
        descriptionLevel: this.formBuilder.array([], Validators.compose([Validators.required, Validators.minLength(1)])),


      }),
      DOC_CONTEXT: this.formBuilder.group({
        subjects: this.formBuilder.array([]),
        writings: this.formBuilder.array([]),
        typologies: this.formBuilder.array([]),
        conservationStates: this.formBuilder.array([]),
        documentaryTraditions: this.formBuilder.array([]),
      }),

      DOC_ACCESS_USE_CONDITIONS: this.formBuilder.group({
        accessConditions: this.formBuilder.array([]),
        languages: this.formBuilder.array([]),
      }),

      DOC_LINKED_DATA: this.formBuilder.group({
        relatedDocs: this.formBuilder.array([]),
      })
    });
    // if (this.service.getObservableUser()) {
    //   this.router.navigate(['/']);
    // }
  }


  returnUrl: string | undefined;
  error = '';
  title = 'FormArray Example in Angular Reactive forms';

// =========End New Elems ===================


  ngOnInit() {
    const href = this.router.url;
    console.log(this.router.url);
    // tslint:disable-next-line:variable-name

    this.pageCreateDoc = href.includes('create');
    if (this.pageCreateDoc) {
      this.setWebPageTitle('Create Doc');
    } else {
      let myTitle: string;
      this.pageCreateDoc = href.includes('update');
      if (this.pageCreateDoc) {
        myTitle = 'Update Doc  ';
      } else {
        myTitle = 'Doc ';
      }
      this.activatedRoute.paramMap.subscribe(params => {
        this.episaIdentifier = params.get('id') || 'id';
        this.getDocById(this.episaIdentifier);
        this.setWebPageTitle(myTitle + this.episaIdentifier);
      });
    }
    // get return url from route parameters or default to '/'
    this.returnUrl = this.activatedRoute.snapshot.queryParams.returnUrl || '/';
    this.isExpanded = true;
  }

  getViewValueFromObject(key: string, myArray: any[]) {
    let i;
    for (i = 0; i < myArray.length; i++) {
      if (key === myArray[i].value) {
        return myArray[i].viewValue;
      }
    }
  }

  setWebPageTitle(myTitle: string) {
    this.titleService.setTitle(myTitle);
  }

  // ========== new Elems ==================

  newTitle(): FormGroup {
    return this.formBuilder.group({
      title: ['', Validators.required],
      type: ['', Validators.required],
    });
  }

  newIdentifier(): FormGroup {
    return this.formBuilder.group({
      identifier: ['', Validators.required],
      type: ['', Validators.required],
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

  newDescriptionLevel(): FormGroup {
    return this.formBuilder.group({
      descriptionLevel: ['', Validators.required],
    });
  }

  // ========== ==================
  getMiddleArrayString(arrayName: string): string {
    let middleArray;

    switch (arrayName) {
      case 'titles':
      case 'descriptionLevel':
      case 'identifiers':
      case 'materials' :
      case 'dimensions':
      case 'quantities':
        middleArray = 'DOC_IDENTITY';
        break;
      case 'subjects':
      case 'writings':
      case 'typologies':
      case 'conservationStates' :
      case 'documentaryTraditions':

        middleArray = 'DOC_CONTEXT';
        break;
      case 'accessConditions' :
      case 'languages':
        middleArray = 'DOC_ACCESS_USE_CONDITIONS';
        break;
      case 'relatedDocs' :
        middleArray = 'DOC_LINKED_DATA';
        break;
    }
    // @ts-ignore
    return middleArray;
  }

  getMiddleArray(arrayName: string): FormArray {
    const middleArray = this.getMiddleArrayString(arrayName);
    return this.docForm.get(middleArray) as FormArray;
  }

  getArrayName(arrayName: string): FormArray {
    return this.getMiddleArray(arrayName).get(arrayName) as FormArray;
  }

  setArrayValue(arrayName: string, resultValue: any) {
    const myArray = this.getArrayName(arrayName);
    const myMiddleArray = this.getMiddleArrayString(arrayName);
    // console.log(resultValue[myMiddleArray][arrayName]);
    const myArrayFromRequest = resultValue[myMiddleArray][arrayName];
    if (myArrayFromRequest.length > 0 && myArray.value.length === 0) {
      this.addElem(arrayName);
    }

    if (myArray.value.length) {
      while (myArray.value.length < myArrayFromRequest.length) {
        this.addElem(arrayName);
      }
      myArray.setValue(myArrayFromRequest);
    }

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
      case'descriptionLevel':
        newElem = this.newDescriptionLevel();
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

  getDocById(id: any) {
    this.service.getDocById(id)
      .subscribe(result => {
          console.log(result);
          if (result.DOC_IDENTITY.titles != null) {
            console.log(this.getArrayName('titles'));
          }
          this.setArrayValue('titles', result);
          this.setArrayValue('identifiers', result);
          this.setArrayValue('accessConditions', result);
          this.setArrayValue('descriptionLevel', result);

          this.setArrayValue('dimensions', result);
          this.setArrayValue('quantities', result);
          this.setArrayValue('typologies', result);
          this.setArrayValue('materials', result);
          this.setArrayValue('documentaryTraditions', result);
          this.setArrayValue('subjects', result);
          this.setArrayValue('relatedDocs', result);
          this.setArrayValue('languages', result);
          this.setArrayValue('writings', result);
          this.setArrayValue('conservationStates', result);
          // const elements = [];
          // for (const relateDoc of result.relatedDocuments) {
          //   const element = {
          //     episaIdentifier: relateDoc.episaIdentifier,
          //     title: relateDoc.title,
          //     dglabIdentifier: relateDoc.dglabIdentifier
          //   };
          //   elements.push(element);
          // }
          // this.dataSource = new MatTableDataSource<Document>(elements);
          // if (this.dataSource.data.length > 0) {
          //   this.haveResults = true;
          // }
        }
      );
  }

  goToHome() {
    this.router.navigate(['/']);
  }

  editDoc() {
    this.router.navigate(['updatedoc/' + this.episaIdentifier]);
  }

  setExpanded(b: boolean) {
    this.isExpanded = b;
  }
}
