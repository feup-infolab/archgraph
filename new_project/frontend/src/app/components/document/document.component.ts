import {Component, OnInit} from '@angular/core';
import {MyService} from '../../service/my.service';
import {ActivatedRoute} from '@angular/router';
import {MatTableDataSource} from '@angular/material/table';
import {Document} from './searchPage/doc-search-page.component';


@Component({
  selector: 'app-my',
  templateUrl: './document.component.html',
  styleUrls: ['./document.component.css']
})
export class DocumentComponent implements OnInit {
  public titles: any[];
  public notes: any[];
  public languages: any[];
  public identifiers: any[];
  public dimensions: any[];
  public descriptionLevel: string;
  public subjects: any[];
  public typologies: any[];
  public relatedEvents: any[];
  public relatedDocs: any[];
  public materials: any[];
  public quantities: any[];
  public conservationStatus: any[];
  public writings: any[];
  public conditions: any[];
  public traditions: any[];
  public accessConditions: any[];
  public documentaryTraditions: any[];
  public episaIdentifier: any;
  public reprodutionConditions: any[];
  public haveResults: boolean | undefined;
  public dataSource: any;
  public columns: any[] = ['episaIdentifier', 'dglab Identifier','title' ];
  public isExpanded: boolean | undefined;

  constructor(
    private service: MyService,
    private route: ActivatedRoute,
  ) {
    this.titles = [];
    this.notes = [];
    this.languages = [];
    this.dimensions = [];
    this.subjects = [];
    this.descriptionLevel = '';
    this.typologies = [];
    this.relatedEvents = [];
    this.relatedDocs = [];
    this.identifiers = [];
    this.materials = [];
    this.quantities = [];
    this.conservationStatus = [];
    this.writings = [];
    this.conditions = [];
    this.traditions = [];
    this.accessConditions = [];
    this.documentaryTraditions = [];
    this.reprodutionConditions = [];
    this.isExpanded = true;

  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.episaIdentifier = params.get('id');
      this.getDocById(this.episaIdentifier);
    });
  }

  getDocById(id: any) {
    this.service.getDocById(id)
      .subscribe(result => {

          console.log(result);
          this.accessConditions = result.accessConditions;
          this.conservationStatus = result.conservationStatus;
          this.dimensions = result.dimensions;
          this.documentaryTraditions = result.documentaryTraditions;
          this.episaIdentifier = result.episaIdentifier;
          this.identifiers = result.identifiers;
          this.languages = result.languages;
          this.materials = result.materials;
          this.quantities = result.quantities;
          this.relatedDocs = result.relatedDocuments;
          this.relatedEvents = result.relatedEvents;
          this.reprodutionConditions = result.reprodutionConditions;
          this.subjects = result.subjects;
          this.titles = result.titles;
          this.typologies = result.typologies;
          this.writings = result.writings;

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
          }
        }
      );
  }

  setExpanded(b: boolean) {
    this.isExpanded = b;
  }
}
