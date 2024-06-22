import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { IProveedor } from '../interfaces/i-proveedor';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProveedorService {

  private urlAPI: string = 'http://localhost:5000/proveedor'; // URL base de la API

  constructor(private http: HttpClient) { }

  getProveedores(): Observable<IProveedor[]> {
    return this.http.get<IProveedor[]>(this.urlAPI)
      .pipe(); // Agregar manejo de errores si es necesario
  }

  getProveedor(rut: string): Observable<IProveedor> {
    const url = `${this.urlAPI}/${rut}`;
    return this.http.get<IProveedor>(url)
      .pipe(); // Agregar manejo de errores si es necesario
  }

  postProveedor(proveedor: IProveedor): Observable<any> {
    const headers = new HttpHeaders({'Content-Type': 'application/json'});
    return this.http.post<any>(this.urlAPI, proveedor, { headers })
      .pipe(); // Agregar manejo de errores si es necesario
  }

  actualizarProveedor(proveedor: IProveedor): Observable<any> {
    const url = `${this.urlAPI}/${proveedor.RutProveedor}`;
    const headers = new HttpHeaders({'Content-Type': 'application/json'});
    return this.http.put<any>(url, proveedor, { headers });
  }

  eliminarProveedor(id: number): Observable<any> {
    const url = `${this.urlAPI}/${id}`;
    return this.http.delete<any>(url)
      .pipe(); // Agregar manejo de errores si es necesario
  }
}
  
