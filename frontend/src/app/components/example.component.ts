import {AfterViewInit, Component, OnChanges, OnInit, ViewChild} from '@angular/core';
import {FormGroup, FormControl} from '@angular/forms';
import {Schema} from '../models/Schema';
import {Utils} from '../models/Utils';
import {MyServiceService} from '../service/my-service.service';
import {CidocSearch} from '../models/CidocSearch';
import {ComboBoxComponent} from '../combo-box/combo-box.component';

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
        });
    }
  }

  getSearchSpecificJson(entity, search) {
    this.service.getSpecificSearchJson(entity, search)
      .subscribe(result => {
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
      });
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
        console.log('ai ai recebi dados do servidor');
        console.log(returned_schema);
        const definitions = returned_schema.definitions;
        const schema = definitions;
        // const schema = definitions[Object.keys(definitions)[0]];
        // this.form.schema = schema;
        const schema2 = {
          $id: 'https://example.com/arrays.schema.json',
          $schema: 'http://json-schema.org/draft-07/schema#',
          description: 'A representation of a person, company, organization, or place',
          type: 'object',
          properties: {
            fruits: {
              type: 'array',
              items: {
                type: 'string'
              }
            },
            vegetables: {
              type: 'array',
              items: {$ref: '#/definitions/veggie'}
            }
          },
          definitions: {
            veggie: {
              type: 'object',
              required: ['veggieName', 'veggieLike'],
              properties: {
                veggieName: {
                  type: 'string',
                  description: 'The name of the vegetable.'
                },
                veggieLike: {
                  type: 'boolean',
                  description: 'Do I like this vegetable?'
                }
              }
            }
          }
        };
        const schema3 = {
          // $ref: '#/definitions/E52_Time_SpanSchema',
          $schema: 'http://json-schema.org/draft-07/schema#',
          type: 'object',
          properties: {
            bb2ca7ccfab44ee49c4594adfde91734: {
              $ref: '#/definitions/E52_Time_SpanSchema',
              title: 'Editing E52_Time_Span <a href=\"/bb2ca7ccfab44ee49c4594adfde91734\">teste</a>'
            }
          },
          definitions: {
            DataObjectSchema: {
              additionalProperties: false,
              properties: {
                name: {
                  title: 'name',
                  type: 'string'
                },
                uid: {
                  title: 'uid',
                  type: 'string'
                }
              },
              required: ['name'],
              type: 'object'
            },
            E52_Time_SpanSchema: {
              additionalProperties: false,
              properties: {
                date: {
                  format: 'date',
                  title: 'date',
                  type: 'string'
                },
                has_value: {
                  items: {
                    $ref: '#/definitions/DataObjectSchema',
                    type: 'object'
                  },
                  type: 'array'
                },
                uid: {
                  title: 'uid',
                  type: 'string'
                },
                name: {
                  title: 'name',
                  type: 'string'
                }
              },
              required: ['date', 'name'],
              type: 'object'
            }
          }
        };

        // this.form.schema = schema3;

        const cloneSchema = {schema3};
        // cloneSchema = Utils.removeUIDs(cloneSchema);
        this.form.schema = this.refactorSchema(returned_schema);

        // delete cloneSchema.uid;
        // Object.keys(cloneSchema).forEach((n, i) => {
        //   const object = {key: n};
        //   this.form.layout.push(object);
        // });
        this.form.layout = ['*'];
        // this.form.layout = [
        //   this.form.schema["definitions"].E52_Time_SpanSchema.properties.name,
        //   this.form.schema["definitions"].E52_Time_SpanSchema.properties.has_value,
        //   this.form.schema["definitions"].E52_Time_SpanSchema.properties.date
        //
        // ];

        // this.form.layout.push('*');

        // });
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
    const properties = {
      entity: {
        $ref: ref,
        title: 'Editing schemaName'

      }
    };
    jsonSchema.properties = properties;

    delete jsonSchema.$ref;
    jsonSchema.type = 'object';
    return jsonSchema;
  }

  deleteUidFromLayout(jsonSchema) {

    //jsonSchema.definitions[schemaName]["properties"]["uid"]
  }

  sendNode(data) {
    this.service.sendNode(data)
      .subscribe(result => {
        this.form.data = result;
        console.log(result);
      });
  }


  onSubmit(a: any) {
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
// {
//   '$id': 'https://example.com/arrays.schema.json',
//   '$schema': 'http://json-schema.org/draft-07/schema#',
//   'description': 'A representation of a person, company, organization, or place',
//   'type': 'object',
//   'properties': {
//   'fruits': {
//     'type': 'array',
//       'items': {
//       'type': 'string'
//     }
//   },
//   'vegetables': {
//     'type': 'array',
//       'items': { '$ref': '#/definitions/veggie' }
//   }
// },
//   'definitions': {
//   'veggie': {
//     'type': 'object',
//       'required': [ 'veggieName', 'veggieLike' ],
//       'properties': {
//       'veggieName': {
//         'type': 'string',
//           'description': 'The name of the vegetable.'
//       },
//       'veggieLike': {
//         'type': 'boolean',
//           'description': 'Do I like this vegetable?'
//       }
//     }
//   }
// }
// }

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


// shema without data____________________________-
// {
//   $schema: 'http://json-schema.org/draft-07/schema#',
//     type: 'object',
//   properties: {
//   vegetables: {
//     $ref: '#/definitions/ola'
//   }
// },
//   definitions: {
//     ola: {
//       type: 'object',
//         required: [ 'veggieName' ],
//         properties: {
//         veggieName: {
//           type: 'string',
//             description: 'The name of the vegetable.'
//         }
//       }
//     }
//   }
// };




