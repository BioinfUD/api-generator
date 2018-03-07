import { Component, OnInit } from '@angular/core';
import { MapaService } from '../../services/mapa.service';
import { Mapa } from '../../models/mapa';
import { Router} from '@angular/router';
import { GlobalsComponent } from '../../globals/globals.component';
import { ConfirmationService } from 'primeng/primeng';

@Component({
  selector: 'app-mapa',
  templateUrl: './mapa-view.component.html',
  styleUrls: []
})
export class MapaComponent implements OnInit {

  mapas: Mapa[];
  mapa: Mapa;

  constructor(private mapaService: MapaService,
      private router: Router, private globals: GlobalsComponent,
      private confirmationService: ConfirmationService) {
      this.globals = globals;
  }

  ngOnInit(): void {
    this.mapaService.getMapas().then(mapas => this.mapas = mapas);
  }

  newMapa(): void {

    this.router.navigate(['/mapa/new']).then(() => null);
    this.globals.currentModule = 'Mapa';
  }

  editar(mapa: Mapa): void {
    this.mapa = mapa;
    this.router.navigate(['/mapa/edit', this.mapa.id ]);
  }

  borrar(mapa: Mapa): void {
    this.confirmationService.confirm({
      message: 'Esta seguro que quiere borrar mapa?',
      accept: () => {
        this.mapaService.delete(mapa.id)
          .then(response => this.mapaService.getMapas().then(mapas => this.mapas = mapas));
      }
    });
  }
}