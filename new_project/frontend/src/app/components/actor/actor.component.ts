import {Component, OnInit} from '@angular/core';
import {FusekiService} from '../../service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-actor',
  templateUrl: './actor.component.html',
  styleUrls: ['./actor.component.css', '../default.css']
})
export class ActorComponent implements OnInit {
  public id: any;
  public identifiers: any[];
  public actor: any[];
  public legalStatus: any[];
  public relatedPlaces: any[];
  public relatedEvents: any[];
  public relatedActors: any[];

  constructor(
    private service: FusekiService,
    private route: ActivatedRoute,
  ) {
    this.identifiers = [];
    this.actor = [];
    this.legalStatus = [];
    this.relatedEvents = [];
    this.relatedActors = [];
    this.relatedPlaces = [];
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
      this.getActorById(this.id);
    });
  }

  getActorById(id: any) {
    this.service.getActorById(id)
      .subscribe(result => {

        console.log(result);
        // this.notes =
        // this.languages =
        // this.titles =
        // this.descriptionLevel =
        // this.dimensions =
        // this.relatedDocs =
        // this.relatedEvents =
      });
  }

}
