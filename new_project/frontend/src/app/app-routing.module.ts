import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {MyComponent} from './components/my.component';


const routes: Routes = [
  { path: '', component: MyComponent }
];

export const routing = RouterModule.forRoot(routes);

