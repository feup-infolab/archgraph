import {MyService} from './service/my.service';
import {AppComponent} from './app.component';
import {MyComponent} from './components/my.component';
import {HttpClientModule} from '@angular/common/http';
import {RouterModule} from '@angular/router';
import {routing} from './app-routing.module';

import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {MatDividerModule} from '@angular/material/divider';
import {MatListModule} from '@angular/material/list';

@NgModule({
    imports: [BrowserModule, RouterModule, HttpClientModule, routing, MatDividerModule, MatListModule],
    providers: [MyService],
    declarations: [AppComponent, MyComponent  ],
    exports: [AppComponent, MyComponent],
    bootstrap: [AppComponent ]
})
export class AppModule {
}
