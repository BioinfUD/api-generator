import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Mapa } from '../models/mapa';

import 'rxjs/add/operator/toPromise';


@Injectable()
export class MapaService {

  private serviceURL = 'http://localhost:5000/api/mapa';
  private headers = new Headers({'Content-Type': 'application/json'});

  constructor(private http: Http) {}

  getMapas(): Promise<Mapa[]> {
    return this.http.get(this.serviceURL)
      .toPromise()
      .then(response => response.json().objects as Mapa[])
      .catch(this.handleError)

  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

  getMapa(id: string): Promise<Mapa> {
    const url = `${this.serviceURL}/${id}`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json() as Mapa)
      .catch(this.handleError);
  }


  update(mapa: Mapa): Promise<Mapa> {
    const url = `${this.serviceURL}/${ mapa.id}`;
    return this.http
      .put(url, JSON.stringify(mapa), {headers: this.headers})
      .toPromise()
      .then(() => mapa)
      .catch(this.handleError);
  }


  create(mapa: Mapa): Promise<Mapa> {
    return this.http
      .post(this.serviceURL, JSON.stringify(mapa), {headers: this.headers})
      .toPromise()
      .then(res => res.json().data as Mapa)
      .catch(this.handleError);
  }

  delete(id: string): Promise<void> {
    const url = `${this.serviceURL}/${id}`;
    return this.http.delete(url, {headers: this.headers})
      .toPromise()
      .then(() => null)
      .catch(this.handleError);
  }

}