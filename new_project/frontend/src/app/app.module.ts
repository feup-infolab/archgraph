import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {RouterModule} from '@angular/router';
import {BrowserModule} from '@angular/platform-browser';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {LayoutModule} from '@angular/cdk/layout';
import {AppComponent} from './app.component';
import {RoutingModule} from './routing/routing.module';

import {MaterialModule} from './material/material.module';
import {MyService} from './service/my.service';
import {DocumentComponent} from './components/document/document.component';
import {FooterComponent} from './components/home/footer/footer.component';
import {HeaderComponent} from './components/home/header/header.component';
import {SidenavListComponent} from './components/home/sidenav-list/sidenav-list.component';
import {HomeComponent} from './components/home/home/home.component';
import {ActorComponent} from './components/actor/actor.component';
import {PlaceComponent} from './components/place/place.component';
import {OrganizationComponent} from './components/organization/organization.component';
import {AdvancedSearchComponent} from './components/search/advanced-search.component';
import {FormsModule} from '@angular/forms';
import {GenericComponent} from './components/event/generic/generic.component';
import {SupportComponent} from './components/event/support/support.component';
import {RestorationComponent} from './components/event/restoration/restoration.component';
import { DocSearchPageComponent } from './components/document/searchPage/doc-search-page.component';
import { ActorSearchPageComponent } from './components/actor/searchPage/actor-search-page.component';
import { EventSearchPageComponent } from './components/event/searchPage/event-search-page.component';
import { OrgSearchPageComponent } from './components/organization/searchPage/org-search-page.component';
import { PlaceSearchPageComponent } from './components/place/searchPage/place-search-page.component';

@NgModule({
    imports: [BrowserModule,
        RouterModule,
        HttpClientModule,
        MaterialModule,
        RoutingModule,
        BrowserAnimationsModule,
        LayoutModule, FormsModule,
    ],
    providers: [MyService],
    declarations: [AppComponent,
        DocumentComponent,
        FooterComponent,
        HeaderComponent,
        SidenavListComponent,
        HomeComponent,
        ActorComponent,
        PlaceComponent,
        OrganizationComponent,
        AdvancedSearchComponent,
        GenericComponent,
        SupportComponent,
        RestorationComponent,
        DocSearchPageComponent,
        ActorSearchPageComponent,
        EventSearchPageComponent,
        OrgSearchPageComponent,
        PlaceSearchPageComponent],
    exports: [AppComponent],
    bootstrap: [AppComponent]
})
export class AppModule {
}
