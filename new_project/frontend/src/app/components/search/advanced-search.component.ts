import {Component, OnInit} from '@angular/core';

@Component({
    selector: 'app-advanced-search',
    templateUrl: './advanced-search.component.html',
    styleUrls: ['./advanced-search.component.css']
})
export class AdvancedSearchComponent implements OnInit {
    public name: any;
    public cperiod: any;
    public fromBirthDate: any;
    public toBirthDate: any;
    public identifier: any;
    public keywords: any;
    public fromDeathDate: any;
    public toDeathDate: any;
    public docIdentifier: any;
    public docIdentifierType: any;
    public title: any;
    public titleType: any;
    public language: any;
    public languageIdentifier: any;
    public personIdentifier: any;

    constructor() {
    }

    ngOnInit(): void {
    }

}
