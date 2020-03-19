import { NgModule } from '@angular/core';
import { MyServiceService } from './service/my-service.service';
import {Bootstrap4FrameworkModule, MaterialDesignFrameworkModule} from 'angular7-json-schema-form';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {ExampleComponent} from './components/example.component';
import {BrowserModule} from '@angular/platform-browser';
import {BrowserAnimationsModule, NoopAnimationsModule} from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import {CommonModule} from '@angular/common';
import {FormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    ExampleComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    MaterialDesignFrameworkModule,
    BrowserAnimationsModule,
    FormsModule,
    CommonModule,
    Bootstrap4FrameworkModule,
    NoopAnimationsModule,
    FlexLayoutModule
  ],
  providers: [MyServiceService],
  bootstrap: [ AppComponent ]
})
export class AppModule { }

