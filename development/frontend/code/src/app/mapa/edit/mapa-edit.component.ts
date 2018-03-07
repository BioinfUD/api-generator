import { Component, OnInit } from '@angular/core';
import { Mapa } from '../../models/mapa';
import { MapaService } from '../../services/mapa.service';
import { Location } from '@angular/common';
import { ActivatedRoute, Params } from '@angular/router';


import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'app-mapa-edit',
  templateUrl: './mapa-edit.component.html',
  styleUrls: []
})
export class MapaEditComponent implements OnInit {

  mapa: Mapa = new Mapa();
  display = false;
  id: string;
  test = new Date('2016-01-05T09:05:05.035Z');

  constructor(private route: ActivatedRoute, private location: Location, private mapaService: MapaService) {

  }

  actualizar(mapa: Mapa): void {
    this.mapaService.update(mapa).then(() => this.display = true);
  }

  ngOnInit() {
    this.route.params.switchMap((params: Params) => this.mapaService.getMapa(params['id']))
      .subscribe(mapa => this.mapa = mapa);
  }

  regresar(): void {
    this.location.back();
  }

  cerrarDialogo(): void {
    this.display = false;
    this.location.back();
  }
}