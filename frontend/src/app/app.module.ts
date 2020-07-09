import {CUSTOM_ELEMENTS_SCHEMA, NgModule} from '@angular/core';
import {MyServiceService} from './service/service-service';
import {Bootstrap4FrameworkModule, MaterialDesignFrameworkModule} from 'angular7-json-schema-form';
import {AppComponent} from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {SearchComponent} from './components/search-component/search-component';
import {BrowserModule} from '@angular/platform-browser';
import {BrowserAnimationsModule, NoopAnimationsModule} from '@angular/platform-browser/animations';
import {FlexLayoutModule} from '@angular/flex-layout';
import {CommonModule} from '@angular/common';
import {FormsModule} from '@angular/forms';
import {ComboBoxComponent} from './combo-box/combo-box.component';
import {RouterModule, Routes} from '@angular/router';
import {EditEntityComponent} from './components/edit/edit-entity/edit-entity.component';
import {MatIconModule} from '@angular/material/icon';
import {
  MatButtonModule,
  MatExpansionModule,
  MatFormFieldModule,
  MatInputModule, MatListModule,
  MatOptionModule,
  MatSelectModule,
  MatSliderModule
} from '@angular/material';
import {EditTemplateComponent} from './components/edit/edit-template/edit-template.component';
import {ViewTemplateComponent} from './components/view/view-template/view-template.component';
import {LayoutComponent} from './components/view/layout-component/layout-component';
import {DocumentComponentComponent} from './components/view/document-component/document-component.component';
import {MatCardModule} from "@angular/material/card";
import {NotifierModule, NotifierOptions} from 'angular-notifier';

const appRoutes: Routes = [
  {path: 'edit-template/:id', component: EditTemplateComponent},
  {path: ':uid', component: EditEntityComponent},
  {path: '', component: SearchComponent},
  {path: 'viewtemplate/:uid', component: ViewTemplateComponent},
  {path: 'uidglab/:uid', component: DocumentComponentComponent}

];
/**
 * Custom angular notifier options
 */
const customNotifierOptions: NotifierOptions = {
  position: {
    horizontal: {
      position: 'right',
      distance: 20
    },
    vertical: {
      position: 'top',
      distance: 20,
      gap: 20
    }
  },
  theme: 'material',
  behaviour: {
    autoHide: 5000,
    onClick: 'hide',
    onMouseover: 'pauseAutoHide',
    showDismissButton: true,
    stacking: 4
  },
  animations: {
    enabled: true,
    show: {
      preset: 'slide',
      speed: 300,
      easing: 'ease'
    },
    hide: {
      preset: 'fade',
      speed: 300,
      easing: 'ease',
      offset: 50
    },
    shift: {
      speed: 300,
      easing: 'ease'
    },
    overlap: 150
  }
};


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
    NotifierModule.withConfig(customNotifierOptions),
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
    MatInputModule,
    MatOptionModule,
    MatSelectModule,
    MatListModule,
    MatCardModule
  ],
  providers: [MyServiceService],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule {
}

