import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';

@Component({
    selector: 'app-restoration',
    templateUrl: './restoration.component.html',
    styleUrls: ['./restoration.component.css']
})
export class RestorationComponent implements OnInit {
    public titles: any[];
    public id: any;


    constructor(
        private service: MyService,
        private route: ActivatedRoute,
    ) {
        this.titles = [];
    }

    ngOnInit() {
        this.route.paramMap.subscribe(params => {
            this.id = params.get('id');
            // this.getNotes(this.id);
            this.getSuppliedTitle(this.id);
        });
    }

    getSuppliedTitle(id: any) {
        this.service.getSuppliedTitle(id)
            .subscribe(result => {
                console.log(result);
                this.titles = result.results.bindings;
            });
    }
}