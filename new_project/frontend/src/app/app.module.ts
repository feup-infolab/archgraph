import {MyService} from './service/my.service';
import {AppComponent} from './app.component';
import {DocumentComponent} from './components/document/document.component';

import {HttpClientModule} from '@angular/common/http';
import {RouterModule} from '@angular/router';

import {NgModule} from '@angular/core';

import {BrowserModule} from '@angular/platform-browser';
import {FooterComponent} from './components/home/footer/footer.component';

import {MaterialModule} from './material/material.module';
import {RoutingModule} from './routing/routing.module';
import {HeaderComponent} from './components/home/header/header.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {LayoutModule} from '@angular/cdk/layout';
import {SidenavListComponent} from './components/home/sidenav-list/sidenav-list.component';
import {HomeComponent} from './components/home/home/home.component';
import {PersonComponent} from './components/person/person.component';
import {EventComponent} from './components/event/event.component';
import {PlaceComponent} from './components/place/place.component';
import {OrganizationComponent} from './components/oranization/organization.component';

@NgModule({
    imports: [BrowserModule,
        RouterModule,
        HttpClientModule,
        MaterialModule,
        RoutingModule,
        BrowserAnimationsModule,
        LayoutModule,
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
        OrganizationComponent],
    exports: [AppComponent],
    bootstrap: [AppComponent]
})
export class AppModule {
}
