import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {CommonModule} from '@angular/common';
import {DocumentComponent} from '../components/document/document.component';
import { HomeComponent} from '../components/home/home/home.component';
import {PersonComponent} from '../components/person/person.component';
import {EventComponent} from '../components/event/event.component';
import {PlaceComponent} from '../components/place/place.component';
import {AdvancedSearchComponent} from '../components/search/advanced-search.component';
import {OrganizationComponent} from '../components/oranization/organization.component';

const routes: Routes = [
    {path: 'home', component: HomeComponent},
    {path: 'doc/:id', component: DocumentComponent},
    {path: 'person/:id', component: PersonComponent},
    {path: 'event/:id', component: EventComponent},
    {path: 'place/:id', component: PlaceComponent},
    {path: 'organization/:id', component: OrganizationComponent},
    {path: 'advancedsearch', component: AdvancedSearchComponent},

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
