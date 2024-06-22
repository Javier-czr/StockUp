import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IUbicacion } from '../interfaces/i-ubicacion';

@Injectable({
  providedIn: 'root'
})
export class UbicacionService {

  private urlAPI = 'http://localhost:5000/ubicacion';

  constructor( private http: HttpClient) { }

  getUbicaciones(): Observable<IUbicacion[]> {
    return this.http.get<IUbicacion[]>(this.urlAPI);
  }

  getUbicacion(id: any): Observable<IUbicacion> {
    const url = `${this.urlAPI}/${id}`;
    return this.http.get<IUbicacion>(url);
  }

  postUbicacion(ubicacion: IUbicacion): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<any>(this.urlAPI, ubicacion, { headers });
  }

  actualizarUbicacion(ubicacion: IUbicacion): Observable<any> {
    const url = `${this.urlAPI}/${ubicacion.IdUbicacion}`;
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.put<any>(url, ubicacion, { headers });
  }

  eliminarUbicacion(id: any): Observable<any> {
    const url = `${this.urlAPI}/${id}`;
    return this.http.delete<any>(url);
  }
}
