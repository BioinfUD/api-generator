import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { EncabezadoComponent } from './encabezado/encabezado.component';
import { NavegacionComponent } from './navegacion/navegacion.component';
import { ContenidoComponent } from './contenido/contenido.component';
import { PieComponent } from './pie/pie.component';
import { MigaComponent } from './miga/miga.component';

import { FormsModule } from '@angular/forms'; // Needed to use ngmodel
import { RoutingModule } from './routing/routing.module';
import { HttpModule } from '@angular/http';


// Primeng Modules
import { ButtonModule} from 'primeng/primeng';
import { DataTableModule, SharedModule } from 'primeng/primeng';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { GlobalsComponent } from './globals/globals.component';


import { ConfirmDialogModule, ConfirmationService } from 'primeng/primeng';
import { DialogModule } from 'primeng/primeng';

// Others
import { DatePickerModule } from 'bizoru-datepicker';


import { MapaComponent } from './mapa/view/mapa-view.component';
import { MapaNewComponent } from './mapa/new/mapa-new.component';
import { MapaEditComponent } from './mapa/edit/mapa-edit.component';
import { MapaService } from './services/mapa.service';



@NgModule({
  declarations: [
    AppComponent,
    EncabezadoComponent,
    NavegacionComponent,
    ContenidoComponent,
    PieComponent,
    MigaComponent,
    MapaComponent,
      MapaNewComponent,
      MapaEditComponent,
    ],
  imports: [
    BrowserModule,
    HttpModule,
    RoutingModule,
    FormsModule,
    ButtonModule,
    DataTableModule,
    SharedModule,
    BrowserAnimationsModule,
    ConfirmDialogModule,
    DialogModule,
    DatePickerModule
  ],
  providers: [
  GlobalsComponent,
  ConfirmationService,
  MapaService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }