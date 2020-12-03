import {Component, OnInit} from '@angular/core';
import {MyService} from '../service/my.service';
import {ActivatedRoute} from '@angular/router';


@Component({
    selector: 'app-my',
    templateUrl: './document.component.html',
    styleUrls: ['./document.component.css']
})
export class DocumentComponent implements OnInit {
    public titles: any[];
    public notes: any[];
    private uid: any;


    constructor(
        private service: MyService,
        private route: ActivatedRoute,
    ) {
        this.titles = [];
        this.notes = [];


    }

    ngOnInit() {
        this.route.paramMap.subscribe(params => {
            this.uid = params.get('uid');
            this.getNotes(this.uid);
            this.getSuppliedTitle(this.uid);
        });
    }


    getSuppliedTitle(uid: any) {
        this.service.getSuppliedTitle(uid)
            .subscribe(result => {
                console.log(result);
                this.titles = result.results.bindings;
            });
    }

    getNotes(uid: any) {
        this.service.getNote(uid)
            .subscribe(result => {
                console.log(result);
                this.notes = result.results.bindings;
            });
    }
}
