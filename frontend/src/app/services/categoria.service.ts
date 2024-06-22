import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ICategoria } from '../interfaces/i-categoria';

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {

  private urlAPI = 'http://localhost:5000/categoria';

  constructor(private http: HttpClient) { }

  getCategorias(): Observable<ICategoria[]> {
    return this.http.get<ICategoria[]>(this.urlAPI).pipe();
  }

  getCategoria(id: any): Observable<ICategoria> {
    const url = `${this.urlAPI}/${id}`;
    return this.http.get<ICategoria>(url);
  }

  postCategoria(categoria: ICategoria): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<any>(this.urlAPI, categoria, { headers })
      .pipe();
  }

  actualizarCategoria(categoria: ICategoria): Observable<any> {
    const url = `${this.urlAPI}/${categoria.IdCategoria}`;
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.put<any>(url, categoria, { headers })
      .pipe();
  }

  eliminarCategoria(id: any): Observable<any> {
    const url = `${this.urlAPI}/${id}`;
    return this.http.delete<any>(url);
  }


}
