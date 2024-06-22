import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { IProducto } from '../interfaces/i-producto';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {
  
  private urlAPI: string = 'http://localhost:5000/producto';

  constructor(private http: HttpClient) {}

  getProductos(): Observable<IProducto[]> {
    return this.http.get<IProducto[]>(this.urlAPI);
  }

  getProducto(id: any): Observable<IProducto> {
    const url = `${this.urlAPI}/${id}`;
    return this.http.get<IProducto>(url);
  }   

  postProducto(producto: IProducto): Observable<any> {
    const headers = new HttpHeaders({'Content-Type': 'application/json'});
    return this.http.post<any>(this.urlAPI, producto, {headers});
  }

  actualizarProducto(producto: IProducto): Observable<any> {
    const url = `${this.urlAPI}/${producto.IdProducto}`;
    const headers = new HttpHeaders({'Content-Type': 'application/json'});
    return this.http.put<any>(url, producto, {headers});
  }

  eliminarProducto(id: any): Observable<any> {
    const url = `${this.urlAPI}/${id}`;
    return this.http.delete<any>(url);
  }

}

