import { NgModule } from '@angular/core';
import { MyServiceService } from './service/my-service.service';
import { MaterialDesignFrameworkModule } from 'angular7-json-schema-form';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {ExampleComponent} from './components/example.component';
import {BrowserModule} from '@angular/platform-browser';
import {BrowserAnimationsModule, NoopAnimationsModule} from '@angular/platform-browser/animations';

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
    NoopAnimationsModule
  ],
  providers: [MyServiceService],
  bootstrap: [ AppComponent ]
})
export class AppModule { }

