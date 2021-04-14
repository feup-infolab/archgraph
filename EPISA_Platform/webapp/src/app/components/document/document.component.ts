import {Component, OnInit} from '@angular/core';
import {FusekiService} from '../../service';
import {ActivatedRoute} from '@angular/router';
import {MatTableDataSource} from '@angular/material/table';
import {Document} from './searchPage/doc-search-page.component';
import { Title } from '@angular/platform-browser';


@Component({
  selector: 'app-my',
  templateUrl: './document.component.html',
  styleUrls: ['./document.component.css', '../default.css']
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
  public conservationStates: any[];
  public writings: any[];
  public conditions: any[];
  public traditions: any[];
  public accessConditions: any[];
  public documentaryTraditions: any[];
  public episaIdentifier: any;
  public reprodutionConditions: any[];
  public haveResults: boolean | undefined;
  public dataSource: any;
  public columns: any[] = ['episaIdentifier', 'dglabIdentifier', 'title'];
  public isExpanded: boolean | undefined;

  constructor(
    private service: FusekiService,
    private route: ActivatedRoute,
    private titleService: Title
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
    this.conservationStates = [];
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
      this.setDocTitle(this.episaIdentifier);
    });
  }
  setDocTitle(title: string) {
    this.titleService.setTitle('Doc '  + title);
  }

  getDocById(id: any) {
    this.service.getDocById(id)
      .subscribe(result => {

          console.log(result);
          this.accessConditions = result.accessConditions;
          this.conservationStates = result.conservationStates;
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
