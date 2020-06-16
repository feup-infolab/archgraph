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
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule, MatExpansionModule, MatFormFieldModule, MatInputModule, MatSliderModule} from '@angular/material';
import { EditTemplateComponent } from './edit-template/edit-template.component';
import { ViewTemplateComponent } from './components/view-template.component';
import { LayoutComponent } from './components/layout.component';
import { DocumentComponentComponent } from './document-component/document-component.component';

const appRoutes: Routes = [
  { path: 'edit-template/:id', component: EditTemplateComponent },
  { path: ':uid', component: EditEntityComponent },
  { path: '', component: SearchComponent },
  { path: 'viewtemplate/:uid', component: ViewTemplateComponent },
  { path: 'eva/:uid', component: DocumentComponentComponent}

];


@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    ComboBoxComponent,
    EditEntityComponent,
    ViewTemplateComponent,
    LayoutComponent,
    EditTemplateComponent,
    DocumentComponentComponent
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
    MatIconModule,
    MatSliderModule,
    MatExpansionModule,
    MatFormFieldModule,
    MatInputModule
  ],
  providers: [MyServiceService],
  bootstrap: [ AppComponent ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }

