import {Component, OnInit} from '@angular/core';

@Component({
    selector: 'app-advanced-search',
    templateUrl: './advanced-search.component.html',
    styleUrls: ['./advanced-search.component.css']
})
export class AdvancedSearchComponent implements OnInit {
    public actorName: any;
    // public identifier: any;
    public actorBirthDateTo: any;
    public actorBirthDateFrom: any;
    public actorDeathDateFrom: any;
    public actorDeathDateTo: any;
    public actorKeywords: any;
    public actorRelatedTo: any;
    public docIdentifier: any;
    public docIdentifierType: any;
    public title: any;
    public titleType: any;
    public language: any;
    public languageIdentifier: any;
    public actorIdentifier: any;
    public actorCulturalPeriod: any;
    public eventName: any;
    public eventType: any;
    public eventLocation: any;
    public eventAddress: any;
    public eventLatitude: any;
    public eventLongitude: any;
    public eventKeywords: any;
    public eventRelatedTo: any;
    public eventCulturalPeriod: any;
    public eventEndDateTo: any;
    public eventEndDateFrom: any;
    public eventStartDateFrom: any;
    public eventIdentifier: any;
    public eventStartDateTo: any;
    public placeName: any;
    public placeIdentifier: any;
    public placeLocation: any;
    public placeAdminDivision: any;
    public placeLatitude: any;
    public placeLongitude: any;
    public placeKeywords: any;
    public placeRelatedTo: any;


    constructor() {
    }

    ngOnInit(): void {
    }

}
