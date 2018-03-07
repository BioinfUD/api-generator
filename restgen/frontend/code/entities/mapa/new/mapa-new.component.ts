import { Component, OnInit } from '@angular/core';
import { Mapa } from '../../models/mapa';
import { MapaService } from '../../services/mapa.service';
import { Location } from '@angular/common';


@Component({
  selector: 'app-mapa-new',
  templateUrl: './mapa-new.component.html',
  styleUrls: []
})
export class MapaNewComponent implements OnInit {

  mapa: Mapa;
  display = false;
  constructor(private mapaService: MapaService, private location: Location) { }

  ngOnInit() {
    this.mapa = new Mapa();
  }

  guardar(mapa: Mapa): void {

    this.mapaService.create(mapa);
    this.display = true;

  }

  regresar(): void {
    this.location.back();
  }

  cerrarDialogo(): void {
    this.display = false;
    this.location.back();
  }
}