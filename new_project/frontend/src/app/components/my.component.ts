import {Component, OnInit} from '@angular/core';
import {MyService} from '../service/my.service';



@Component({
    selector: 'app-my',
    templateUrl: './my.component.html',
    styleUrls: ['./my.component.css']
})
export class MyComponent implements OnInit {
    public titles: any[];
    public notes: any[];


    constructor(
        private service: MyService) {
        this.titles = [];
        this.notes = [];

    }

    ngOnInit() {
        this.getSuppliedTitle();
        this.getNotes()
    }

    getSuppliedTitle() {
        this.service.getSuppliedTitle()
            .subscribe(result => {
                console.log(result);
                this.titles = result.results.bindings;
            });
    }

    getNotes() {
        this.service.getNote()
            .subscribe(result => {
                console.log(result);
                this.notes = result.results.bindings;
            });
    }
}
