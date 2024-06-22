import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NotificacionService {

  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  getNotificaciones(): Observable<any> {
    return this.http.get(`${this.apiUrl}/notificacion`);
  }

  verificarProductos(): Observable<any> {
    return this.http.post(`${this.apiUrl}/verificar_productos`, {});
  }
  
}
