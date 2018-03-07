import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CommonModule } from '@angular/common';

import { MapaComponent } from '../mapa/view/mapa-view.component';
import { MapaNewComponent } from '../mapa/new/mapa-new.component';
import { MapaEditComponent } from '../mapa/edit/mapa-edit.component';


const routes: Routes = [
  { path: 'mapa', component: MapaComponent },
  { path: 'mapa/new', component: MapaNewComponent },
  { path: 'mapa/edit/:id', component: MapaEditComponent },
  ];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule],
  declarations: []
})
export class RoutingModule { }