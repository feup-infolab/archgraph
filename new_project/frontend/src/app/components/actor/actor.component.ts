import {Component, OnInit} from '@angular/core';
import {MyService} from '../../service/my.service';
import {ActivatedRoute} from '@angular/router';

@Component({
    selector: 'app-actor',
    templateUrl: './actor.component.html',
    styleUrls: ['./actor.component.css']
})
export class ActorComponent implements OnInit {
    private id: any;
    public identifiers: any[];
    public actor: any[];
    public legalStatus: any[];
    public relatedPlaces: any[];
    public relatedEvents: any[];
    public relatedActors: any[];

    constructor(
        private service: MyService,
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
            this.getSuppliedTitle(this.id);
            // this.getAllDocById(this.id);
        });
    }

    getSuppliedTitle(id: any) {
        this.service.getSuppliedTitle(id)
            .subscribe(result => {
                console.log(result);
                this.identifiers = result.results.bindings;
            });
    }

    getAllActorById(id: any) {
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
