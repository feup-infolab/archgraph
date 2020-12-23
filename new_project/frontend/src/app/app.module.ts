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
import {PersonComponent} from './components/person/person.component';
import {EventComponent} from './components/event/event.component';
import {PlaceComponent} from './components/place/place.component';
import {OrganizationComponent} from './components/oranization/organization.component';
import { AdvancedSearchComponent } from './components/search/advanced-search.component';
import {FormsModule} from "@angular/forms";

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
        PersonComponent,
        EventComponent,
        PlaceComponent,
        OrganizationComponent,
        AdvancedSearchComponent],
    exports: [AppComponent],
    bootstrap: [AppComponent]
})
export class AppModule {
}
