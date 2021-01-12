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
    private id: any;
    private dimensions: any[];
    private descriptionLevel: string;
    private subjects: any[];
    private typologies: any[];
    private relatedEvents: any[];
    private relatedDocs: any[];

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

    // getNotes(id: any) {
    //     this.service.getNote(id)
    //         .subscribe(result => {
    //             console.log(result);
    //             this.notes = result.results.bindings;
    //         });
    // }

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
