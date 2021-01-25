import {Component, OnInit} from '@angular/core';

@Component({
    selector: 'app-advanced-search',
    templateUrl: './advanced-search.component.html',
    styleUrls: ['./advanced-search.component.css']
})
export class AdvancedSearchComponent implements OnInit {
    // actor
    public actorName: any;
    public actorBirthDateTo: any;
    public actorBirthDateFrom: any;
    public actorDeathDateFrom: any;
    public actorDeathDateTo: any;
    public actorKeywords: any;
    public actorRelatedTo: any;
    public actorIdentifier: any;
    public actorCulturalPeriod: any;
    // document
    public docDescriptionLevel: any;
    public docReferenceCode: any;
    public docKeywords: any;
    public docRelatedTo: any;
    public docProdDateFrom: any;
    public docProdDateTo: any;
    public docInterventionStartDateFrom: any;
    public docInterventionStartDateTo: any;
    public docInterventionEndDateFrom: any;
    public docInterventionEndDateTo: any;
    public docCuratorName: any;
    public docCreationDateFrom: any;
    public docCreationDateTo: any;
    //  event
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
    // place
    public placeName: any;
    public placeIdentifier: any;
    public placeLocation: any;
    public placeAdminDivision: any;
    public placeLatitude: any;
    public placeLongitude: any;
    public placeKeywords: any;
    public placeRelatedTo: any;
    // organization
    public orgName: any;
    public orgIdentifier: any;
    public orgCulturalPeriod: any;
    public orgLatitude: any;
    public orgLongitude: any;
    public orgKeywords: any;
    public orgRelatedTo: any;
    public orgLocation: any;
    public orgBuildDateFrom: any;
    public orgBuildDateTo: any;

    constructor() {
    }

    ngOnInit(): void {
    }

}
