import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {DocumentComponent} from './components/document.component';


const routes: Routes = [
  { path: 'documento/:id', component: DocumentComponent }
];

export const routing = RouterModule.forRoot(routes);

