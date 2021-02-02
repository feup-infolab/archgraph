import {Component, OnInit} from '@angular/core';
import {MyService} from '../../service/my.service';
import {ActivatedRoute} from '@angular/router';


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
    private id: any;
    public dimensions: any[];
    public descriptionLevel: string;
    public subjects: any[];
    public typologies: any[];
    public relatedEvents: any[];
    public relatedDocs: any[];
    public materials: any[];
    public quantities: any[];
    public conservation: any[];
    public writings: any[];
    public conditions: any[];
    public traditions: any[];

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
        this.conservation = [];
        this.writings = [];
        this.conditions = [];
        this.traditions = [];
    }

    ngOnInit() {
        this.route.paramMap.subscribe(params => {
            this.id = params.get('id');
            // this.getNotes(this.id);
            this.getSuppliedTitle(this.id);
            this.getAllDocById(this.id);
        });
    }

    getSuppliedTitle(id: any) {
        this.service.getSuppliedTitle(id)
            .subscribe(result => {
                console.log(result);
                this.titles = result.results.bindings;
            });
    }

    getAllDocById(id: any) {
        this.service.getAllDocById(id)
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
