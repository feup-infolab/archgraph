import { NgModule } from '@angular/core';
import { MyServiceService } from './service/my-service.service';
import { MaterialDesignFrameworkModule } from 'angular7-json-schema-form';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {ExampleComponent} from './components/example.component';
import { MyComponentComponent } from './components/my-component.component';
import {BrowserModule} from '@angular/platform-browser';

@NgModule({
  declarations: [
    AppComponent,
    ExampleComponent,
    MyComponentComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    MaterialDesignFrameworkModule
  ],
  providers: [MyServiceService],
  bootstrap: [ AppComponent ]
})
export class AppModule { }

