import {AfterViewInit, Component, OnChanges, OnInit, ViewChild} from '@angular/core';
import {FormGroup, FormControl} from '@angular/forms';
import {Schema} from '../models/Schema';
import {Utils} from '../models/Utils';
import {MyServiceService} from '../service/my-service.service';
import {CidocSearch} from '../models/CidocSearch';
import {ComboBoxComponent} from '../combo-box/combo-box.component';
import {animate, query, stagger, style, transition, trigger} from '@angular/animations';




@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})

export class ExampleComponent implements OnInit {

  constructor(private service: MyServiceService) {
  }

  @ViewChild(ComboBoxComponent) comboBoxReference;
  searched = '';
  searchResult = {};
  searchResultArray: Array<CidocSearch> = new Array<CidocSearch>();
  searchResultS: CidocSearch;
  searchLabels: [];
  selectedEntity: string;
  searchName = '';
  searchUID = '';
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
    schema: {},
    data: {},
    layout: []
  };
  itemList = ['E1_CRM_Entity', 'E2_Temporal_Entity', 'E3_Condition_State', 'E4_Period', 'E5_Event',
    'E6_Destruction', 'E7_Activity', 'E8_Acquisition', 'E9_Move',
    'E10_Transfer_of_Custody', 'E11_Modification', 'E12_Production',
    'E13_Attribute_Assignment', 'E14_Condition_Assessment',
    'E15_Identifier_Assignment', 'E16_Measurement', 'E17_Type_Assignment',
    'E18_Physical_Thing', 'E19_Physical_Object', 'E20_Biological_Object',
    'E21_Person', 'E22_Human_Made_Object', 'E24_Physical_Human_Made_Thing',
    'E25_Human_Made_Feature', 'E26_Physical_Feature', 'E27_Site',
    'E28_Conceptual_Object', 'E29_Design_or_Procedure', 'E30_Right',
    'E31_Document', 'E32_Authority_Document', 'E33_Linguistic_Object',
    'E34_Inscription', 'E35_Title', 'E36_Visual_Item', 'E37_Mark', 'E39_Actor',
    'E41_Appellation', 'E42_Identifier', 'E52_Time_Span', 'E53_Place',
    'E54_Dimension', 'E55_Type', 'E56_Language', 'E57_Material',
    'E58_Measurement_Unit', 'E63_Beggining_of_Existence', 'E64_End_of_Existence',
    'E65_Creation', 'E66_Formation', 'E67_Birth', 'E68_Dissolution', 'E69_Death',
    'E70_Thing', 'E71_Human_Made_Thing', 'E72_Legal_Object',
    'E73_Information_Object', 'E74_Group', 'E77_Persistent_Item',
    'E78_Curated_Holding', 'E79_Part_Addition', 'E80_Part_Removal',
    'E81_Transformation', 'E83_Type_Creation', 'E85_Joining', 'E86_Leaving',
    'E87_Curation_Activity', 'E89_Propositional_Object', 'E90_Symbolic_Object',
    'E92_Spacetime_Volume', 'E93_Presence', 'E96_Purchase', 'E97_Monetary_Amount',
    'E98_Currency', 'E99_Product_Type'];

  headers = ['name', 'uid', 'labels'];
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
    this.searchResultArray = [];
    this.selectedEntity = this.comboBoxReference.inputItem;
    if (this.selectedEntity !== '') {
      this.getSearchSpecificJson(this.selectedEntity, search);
    } else {
      this.service.getSearchJson(search)
        .subscribe(result => {
          this.changeContent(result)
      });
    }
  }

  getSearchSpecificJson(entity, search) {
    this.service.getSpecificSearchJson(entity, search)
      .subscribe(result => {
          this.changeContent(result)
      });
  }
  changeContent(result) {
        this.searchResult = result;
        const entries = Object.entries(result);
        for (const entry of result) {
          const entries2 = Object.entries(entry);
          for (const key of Object.keys(entry)) {
            if (key === 'name') {
              this.searchName = entry[key];
            } else if (key === 'uid') {
              this.searchUID = entry[key];
            } else if (key === 'labels') {
              this.searchLabels = entry[key];
            }
          }
          this.searchResultS = new CidocSearch(this.searchName, this.searchUID, this.searchLabels);
          this.searchResultArray.push(this.searchResultS);
        }
        this.loadSearch = true;

  }

  ngOnInit() {

  }

  getDataNode(uid) {
    this.service.getDataNode(uid)
      .subscribe(result => {
        this.form.data = result;
        console.log(result);
        this.load = true;
      });
  }

  getSchemaNode(uid) {
    this.service.getSchemaNode(uid)
      .subscribe(returned_schema => {
        this.form.layout = [];
        console.log(returned_schema);
        this.form.schema = this.refactorSchema(returned_schema);
        this.form.layout = ['*'];
        // const button1 = {
        //   type: 'submit',
        //   title: 'Submit',
        //   onClick(evt) {
        //     sen
        //     evt.preventDefault();
        //     alert('Thank you!');
        //   }
        // this.getDataNode(this.uid);
        this.load = true;
      });
  }

  refactorSchema(jsonSchema) {
    const ref = jsonSchema.$ref;
    const path = ref.split('/');
    const schemaName = path[2];
    const properties = {};
    properties[this.uid] = {
        $ref: ref,
        title: 'Editing schemaName'
    };
    jsonSchema.properties = properties;
    jsonSchema.desc = "Description";

    delete jsonSchema.$ref;
    const schemaEntity = jsonSchema.definitions[schemaName];

    delete schemaEntity.properties.uid;
    jsonSchema.type = 'object';
    return jsonSchema;

  }
  sendNode(data) {
    this.service.sendNode(data)
      .subscribe(result => {
        this.form.data = result;
        console.log(result);
      });
  }


  onSubmit(a: any) {
    console.log(a);
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
// const schema3 = {
//           $schema: 'http://json-schema.org/draft-07/schema#',
//           type: 'object',
//           properties: {
//             bb2ca7ccfab44ee49c4594adfde91734: {
//               $ref: '#/definitions/E52_Time_SpanSchema',
//               title: 'Editing E52_Time_Span <a href=\"/bb2ca7ccfab44ee49c4594adfde91734\">teste</a>'
//             }
//           },
//
//           definitions: {
//             DataObjectSchema: {
//               additionalProperties: false,
//               properties: {
//                 name: {
//                   title: 'name',
//                   type: 'string'
//                 },
//                 uid: {
//                   title: 'uid',
//                   type: 'string'
//                 }
//               },
//               required: ['name'],
//               type: 'object'
//             },
//             E52_Time_SpanSchema: {
//               additionalProperties: false,
//               properties: {
//                 date: {
//                   format: 'date',
//                   title: 'date',
//                   type: 'string'
//                 },
//                 has_value: {
//                   items: {
//                     $ref: '#/definitions/DataObjectSchema',
//                     type: 'object'
//                   },
//                   type: 'array'
//                 },
//                 uid: {
//                   title: 'uid',
//                   type: 'string'
//                 },
//                 name: {
//                   title: 'name',
//                   type: 'string'
//                 }
//               },
//               required: ['date', 'name'],
//               type: 'object'
//             }
//           }
//         };

// data
// {
//   'fruits': [ 'apple' ],
//   'vegetables': [
//   {
//     'veggieName': 'potato',
//     'veggieLike': true
//   },
//   {
//     'veggieName': 'broccoli',
//     'veggieLike': false
//   }
// ]
// }



