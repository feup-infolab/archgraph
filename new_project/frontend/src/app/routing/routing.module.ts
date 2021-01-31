import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {CommonModule} from '@angular/common';
import {DocumentComponent} from '../components/document/document.component';
import {HomeComponent} from '../components/home/home/home.component';
import {ActorComponent} from '../components/actor/actor.component';
import {PlaceComponent} from '../components/place/place.component';
import {AdvancedSearchComponent} from '../components/search/advanced-search.component';
import {OrganizationComponent} from '../components/organization/organization.component';
import {RestorationComponent} from '../components/event/restoration/restoration.component';
import {SupportComponent} from '../components/event/support/support.component';
import {GenericComponent} from '../components/event/generic/generic.component';

const routes: Routes = [
    {path: 'home', component: HomeComponent},
    {path: 'doc/:id', component: DocumentComponent},
    {path: 'actor/:id', component: ActorComponent},
    {path: 'event/conservation_restoration/:id', component: RestorationComponent},
    {path: 'event/support/:id', component: SupportComponent},
    {path: 'event/generic/:id', component: GenericComponent},
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
