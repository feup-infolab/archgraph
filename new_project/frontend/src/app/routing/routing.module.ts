import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {CommonModule} from '@angular/common';
import {DocumentComponent} from '../components/document/document.component';
import {HomeComponent} from '../components/home/home/home.component';
import {ActorComponent} from '../components/actor/actor.component';
import {PlaceComponent} from '../components/place/place.component';
import {AdvancedSearchComponent} from '../components/advancedSearch/advanced-search.component';
import {OrganizationComponent} from '../components/organization/organization.component';
import {RestorationComponent} from '../components/event/restoration/restoration.component';
import {SupportComponent} from '../components/event/support/support.component';
import {GenericComponent} from '../components/event/generic/generic.component';
import {DocSearchPageComponent} from '../components/document/searchPage/doc-search-page.component';
import {ActorSearchPageComponent} from '../components/actor/searchPage/actor-search-page.component';
import {EventSearchPageComponent} from '../components/event/searchPage/event-search-page.component';
import {PlaceSearchPageComponent} from '../components/place/searchPage/place-search-page.component';
import {OrgSearchPageComponent} from '../components/organization/searchPage/org-search-page.component';
import {TableComponent} from '../components/view/table.component';

const routes: Routes = [
    {path: 'home', component: HomeComponent},
    {path: 'doc/:uid', component: DocumentComponent},
    {path: 'searchdoc', component: DocSearchPageComponent},
    {path: 'actor/:uid', component: ActorComponent},
    {path: 'searchactor', component: ActorSearchPageComponent},
    {path: 'event/conservation_restoration/:uid', component: RestorationComponent},
    {path: 'event/support/:uid', component: SupportComponent},
    {path: 'event/generic/:uid', component: GenericComponent},
    {path: 'searchaevent', component: EventSearchPageComponent},
    {path: 'place/:uid', component: PlaceComponent},
    {path: 'searchplace', component: PlaceSearchPageComponent},
    {path: 'organization/:uid', component: OrganizationComponent},
    {path: 'searchorganization', component: OrgSearchPageComponent},
    {path: 'advancedsearch', component: AdvancedSearchComponent},
    {path: 'table', component: TableComponent},

    {path: '', redirectTo: '/home', pathMatch: 'full'},
];

@NgModule({
    declarations: [],
    imports: [
        CommonModule,
        RouterModule.forRoot(routes)
    ],
    exports: [RouterModule]
})


export class RoutingModule {
}
