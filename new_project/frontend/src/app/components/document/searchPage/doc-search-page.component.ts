import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';
import {MatTableDataSource} from '@angular/material/table';
import {element} from "protractor";

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
    public columns: any[] = ['episaIdentifier', 'title', 'dglabIdentifier', ];

    constructor(
        private service: MyService,
        private route: ActivatedRoute,
    ) {
    }

    ngOnInit() {
        this.route.paramMap.subscribe(params => {
            // this.id = params.get('id');
            // this.referenceCode = '111';
            // this.getDocSummary(this.referenceCode);
            // this.getAllDocById(this.id);
        });
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

    // getActorSummary($event: MouseEvent) {
    //   console.log('result');
    //   this.service.getActorSummary(this.identifier)
    //       .subscribe(result => {
    //         console.log(result);
    //         this.dataSource = new MatTableDataSource<PeriodicElement>(ELEMENT_DATA);
    //         if (this.dataSource.data.length > 0) {
    //           this.haveResults = true;
    //         }
    //         // this.identifiers = result.results.bindings;
    //       });
    // }

    setHaveResults($event: MouseEvent) {
        this.haveResults = false;

    }
}

export interface Document {
    episaIdentifier: string;
    title: string;
    dglabIdentifier: string;
}


export interface PeriodicElement {
    name: string;
    position: number;
    weight: number;
    symbol: string;
}

const ELEMENT_DATA: PeriodicElement[] = [
    {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H'},
    {position: 2, name: 'Helium', weight: 4.0026, symbol: 'He'},
    {position: 3, name: 'Lithium', weight: 6.941, symbol: 'Li'},
    {position: 4, name: 'Beryllium', weight: 9.0122, symbol: 'Be'},
    {position: 5, name: 'Boron', weight: 10.811, symbol: 'B'},
    {position: 6, name: 'Carbon', weight: 12.0107, symbol: 'C'},
    {position: 7, name: 'Nitrogen', weight: 14.0067, symbol: 'N'},
    {position: 8, name: 'Oxygen', weight: 15.9994, symbol: 'O'},
    {position: 9, name: 'Fluorine', weight: 18.9984, symbol: 'F'},
    {position: 10, name: 'Neon', weight: 20.1797, symbol: 'Ne'},
    {position: 11, name: 'Sodium', weight: 22.9897, symbol: 'Na'},
    {position: 12, name: 'Magnesium', weight: 24.305, symbol: 'Mg'},
    {position: 13, name: 'Aluminum', weight: 26.9815, symbol: 'Al'},
    {position: 14, name: 'Silicon', weight: 28.0855, symbol: 'Si'},
    {position: 15, name: 'Phosphorus', weight: 30.9738, symbol: 'P'},
    {position: 16, name: 'Sulfur', weight: 32.065, symbol: 'S'},
    {position: 17, name: 'Chlorine', weight: 35.453, symbol: 'Cl'},
    {position: 18, name: 'Argon', weight: 39.948, symbol: 'Ar'},
    {position: 19, name: 'Potassium', weight: 39.0983, symbol: 'K'},
    {position: 20, name: 'Calcium', weight: 40.078, symbol: 'Ca'},
];
