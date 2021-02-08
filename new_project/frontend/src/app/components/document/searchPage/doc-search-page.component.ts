import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';
import {MatTableDataSource} from '@angular/material/table';

export interface Document {
    episaIdentifier: string;
    title: string;
    dglabIdentifier: string;
}


@Component({
    selector: 'app-doc-search-page',
    templateUrl: './doc-search-page.component.html',
    styleUrls: ['./doc-search-page.component.css']
})
export class DocSearchPageComponent implements OnInit {
    // document
    public descriptionLevel: any;
    public referenceCode: any;
    public keywords: any;
    public relatedTo: any;
    public prodDateFrom: any;
    public prodDateTo: any;
    public interventionStartDateFrom: any;
    public interventionStartDateTo: any;
    public interventionEndDateFrom: any;
    public interventionEndDateTo: any;
    public curatorName: any;
    public creationDateFrom: any;
    public creationDateTo: any;
    public haveResults: boolean | undefined;
    public dataSource: any;
    public columns: any[] = ['episaIdentifier', 'title', 'dglabIdentifier'];

    constructor(
        private service: MyService,
        private route: ActivatedRoute,
    ) {
    }

    ngOnInit() {
            // this.referenceCode = '111';
            // this.getDocSummary(this.referenceCode);
            // this.getAllDocById(this.id);
    }


    getDocSummary($event: MouseEvent) {
        // this.dataSource = new MatTableDataSource<PeriodicElement>(ELEMENT_DATA);
        // if (this.dataSource.data.length > 0) {
        //     this.haveResults = true;
        // }
        this.service.getDocSummary(this.referenceCode)
            .subscribe(result => {
                console.log(result);
                // tslint:disable-next-line:no-shadowed-variable
                const elements = [];
                // tslint:disable-next-line:no-shadowed-variable
                const element = {
                    episaIdentifier: result.episaIdentifier,
                    title: result.title,
                    dglabIdentifier: result.dglabIdentifier
                };
                elements.push(element);
                this.dataSource = new MatTableDataSource<Document>(elements);
                if (this.dataSource.data.length > 0) {
                    this.haveResults = true;
                }
                //         // this.identifiers = result.results.bindings;
                //       });
                // this.identifiers = result.results.bindings;
            });
    }

    setHaveResults($event: MouseEvent) {
        this.haveResults = false;
    }
}
