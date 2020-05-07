import {CUSTOM_ELEMENTS_SCHEMA, NgModule} from '@angular/core';
import { MyServiceService } from './service/my-service.service';
import {Bootstrap4FrameworkModule, MaterialDesignFrameworkModule} from 'angular7-json-schema-form';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {SearchComponent} from './components/search.component';
import {BrowserModule} from '@angular/platform-browser';
import {BrowserAnimationsModule, NoopAnimationsModule} from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import {CommonModule} from '@angular/common';
import {FormsModule} from '@angular/forms';
import {ComboBoxComponent} from './combo-box/combo-box.component';
import { RouterModule, Routes } from '@angular/router';
import { EditEntityComponent } from './components/edit-entity.component';
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from '@angular/material';
import { ViewTemplateComponent } from './components/view-template.component';
import { LayoutComponent } from './components/layout.component';

const appRoutes: Routes = [
  { path: '', component: SearchComponent },
  { path: 'viewtemplate/:uid', component: ViewTemplateComponent },
  { path: ':uid', component: EditEntityComponent }

];


@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    ComboBoxComponent,
    EditEntityComponent,
    ViewTemplateComponent,
    LayoutComponent
  ],
  imports: [
    RouterModule.forRoot(
      appRoutes,
      {enableTracing: true} // <-- debugging purposes only
    ),
    BrowserModule,
    HttpClientModule,
    MaterialDesignFrameworkModule,
    BrowserAnimationsModule,
    FormsModule,
    CommonModule,
    Bootstrap4FrameworkModule,
    NoopAnimationsModule,
    FlexLayoutModule,
    MatButtonModule,
    MatIconModule
  ],
  providers: [MyServiceService],
  bootstrap: [ AppComponent ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }

