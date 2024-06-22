import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Cambio {
  IdCambio: number;
  fechaCambio: string;
  DescripcionCambio: string;
}

@Injectable({
  providedIn: 'root'
})
export class HistorialCambioService {

  private apiUrl = 'http://localhost:5000/historialcambio';

  constructor(private http: HttpClient) { }

  obtenerCambios(fecha?: string, descripcion?: string): Observable<Cambio[]> {
    let params = new HttpParams();
    if (fecha) {
      params = params.append('fecha', fecha);
    }
    if (descripcion) {
      params = params.append('descripcion', descripcion);
    }
    return this.http.get<Cambio[]>(this.apiUrl, { params });
  }
}
