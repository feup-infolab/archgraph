import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';

@Component({
    selector: 'app-generic',
    templateUrl: './generic.component.html',
    styleUrls: ['./generic.component.css']
})
export class GenericComponent implements OnInit {
    public identifiers: any[];
    public name: any;
    public id: any;
    public titles: any[] | undefined;
    public relatedActors: any[];
    public relatedEvents: any[];

    constructor(
        private service: MyService,
        private route: ActivatedRoute,
    ) {
        this.identifiers = [];
        this.relatedActors = [];
        this.relatedEvents = [];
    }

    ngOnInit() {
        this.route.paramMap.subscribe(params => {
            this.id = params.get('id');
            // this.getNotes(this.id);
            // this.getSuppliedTitle(this.id);
        });
    }
}
