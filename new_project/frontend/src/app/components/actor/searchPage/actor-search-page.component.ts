import {Component, OnInit} from '@angular/core';
import {MyService} from '../../../service/my.service';
import {ActivatedRoute} from '@angular/router';

@Component({
    selector: 'app-actor-search-page',
    templateUrl: './actor-search-page.component.html',
    styleUrls: ['./actor-search-page.component.css']
})
export class ActorSearchPageComponent implements OnInit {
    public Name: any;
    public BirthDateTo: any;
    public BirthDateFrom: any;
    public DeathDateFrom: any;
    public DeathDateTo: any;
    public Keywords: any;
    public RelatedTo: any;
    public Identifier: any;
    public CulturalPeriod: any;
    public episaIdentifier: any;

    constructor(
        private service: MyService,
        private route: ActivatedRoute,
    ) {
    }

    ngOnInit() {
        this.route.paramMap.subscribe(params => {
            // this.id = params.get('id');
            this.getActorSummary(this.Identifier);
            // this.getAllDocById(this.id);
        });
    }

    getActorSummary(Identifier: any) {
        this.service.getActorSummary(Identifier)
            .subscribe(result => {
                console.log(result);
                // this.identifiers = result.results.bindings;
            });
    }
}
